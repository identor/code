# This class creates a single card of a deck. For simplicity, assume that Ace has a value of 1
# and has the lowest value. King has a value of 13 and has the highest value.
# Order of suits are clubs, spades, hearts and diamonds in ascending order
class Card:
    # spade ("\u2660")
    # diamond ("\u2666")
    # heart ("\u2764")
    # clover ("\u2618")
    suits = ["\u2618", "\u2660", "\u2764", "\u2666"]
    ranks = ["null", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]    

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranks[self.rank] + " " + self.suits[self.suit])    
    
    def __repr__(self):
        return self.__str__()

    def __cmp__(self, other):
        # check ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # ranks are the same... check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # ranks are the same... it's a tie
        return 0
    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __le__(self, other):
        return self.__cmp__(other) < 0

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __ge__(self, other):
        return self.__cmp__(other) >= 0

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + str(self.cards[i]) + "\n"
        return s 

    # shuffles the deck
    def shuffle(self):
        import random
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = random.randrange(i, num_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    # removes and return the top card of the deck
    def popCard(self):
        return self.cards.pop(0)
#-------------------------------------------------------------------------------
class Hand:
    types = ["high_card", "pair", "two_pair", "trio", "straight", "flush",
             "full", "quad", "straight_flush"]
    
    def __init__(self, card_list = []):
        self.cards = sorted(card_list)
        self.cards.reverse()
        self.type = -1

    # removed the cards present in the current hand returns a sorted copy
    def removed(self, cards):
        result = sorted(self.cards)
        for i in range(len(cards)):
            result.remove(cards[i])
        return result
    
    def __str__(self):
        s = ""
        s = s + "Hand Type: " + self.getHandType
        for i in range(len(self.cards)):
            s = s + str(self.cards[i]) + "\n"
        return s
    
    def getHandType(self):
        cards = []
        if len(self.getStraightFlush()) == 5:
            cards = self.getStraightFlush()
            self.type = 8
        elif len(self.getQuad()) == 4:
            cards = self.getQuad()
            self.type = 7
        elif len(self.getFull()) == 5:
            cards = self.getFull()
            self.type = 6
        elif len(self.getFlush()) == 5:
            cards = self.getFlush()
            self.type = 5
        elif len(self.getStraight()) == 5:
            cards = self.getStraight()
            self.type = 4
        elif len(self.getTrio()) == 3:
            cards = self.getTrio()
            self.type = 3
        elif len(self.getTwoPair()) == 4:
            cards = self.getTwoPair()
            self.type = 2
        elif len(self.getPair()) == 2:
            cards = self.getPair()
            self.type = 1
        else:
            self.type = 0
            
        r = self.removed(cards)
        r.sort()
        r.reverse()
        cards.extend(r)
        self.cards = cards
        return self.types[self.type] + ": " + cards[0].__str__()

    def getPair(self):
        cards = sorted(self.cards)
        result = [Card(), Card()]
        card_len = len(cards)
        i = len(Card.ranks);
        while i > 0:
            same_rank = 0
            for j in range(card_len):
                if i == cards[j].rank:
                    result[same_rank] = cards[j]
                    same_rank = same_rank+1
                    # highest pair is achieved
                    if same_rank == 2:
                        return result
            i = i - 1
        # failure in detecting a pair
        result = []
        return result

    def getTrio(self):        
        cards = sorted(self.cards)
        result = [Card(), Card(), Card()]
        card_len = len(cards)
        i = len(Card.ranks);
        while i > 0:
            same_rank = 0
            for j in range(card_len):
                if i == cards[j].rank:
                    result[same_rank] = cards[j]
                    same_rank = same_rank+1
                    # highest trio is achieved
                    if same_rank == 3:
                        return result
            i = i - 1
        # failure in detecting a trio
        result = []
        return result

    def getQuad(self):
        cards = sorted(self.cards)
        result = [Card(), Card(), Card(), Card()]
        card_len = len(cards)
        i = len(Card.ranks)
        while i > 0:
            same_rank = 0
            for j in range(card_len):
                if i == cards[j].rank:
                    result[same_rank] = cards[j]
                    same_rank = same_rank+1
                    # highest quad is achieved
                    if same_rank == 4:
                        return result
            i = i - 1
        # failure in detecting a quad
        result = []
        return result

    def getFull(self):
        result = [Card(), Card(), Card(), Card(), Card()]
        # t represents the highest trio
        t = self.getTrio()
        if len(t) != 3:
            # failure in detecting a fullhouse: there are no trios in the current cards
            return []
        # t_rem is a list where the highest trio is removed from the current cards
        t_rem = self.removed(t)
        result[:len(t)] = t
        cards = sorted(t_rem) 
        card_len = len(cards)
        i = len(Card.ranks)
        while i > 0:
            same_rank = 0
            for j in range(card_len):
                if i == cards[j].rank:
                    result[same_rank+3] = cards[j]
                    same_rank = same_rank+1
                    # fullhouse is achieved
                    if same_rank == 2:
                        return result
            i = i - 1
        # failure in detecting a fullhouse
        result = []
        return result

    def getTwoPair(self):
        result = [Card(), Card(), Card(), Card()]
        # p represents the highest trio
        p = self.getPair()
        if len(p) != 2:
            # failure in detecting a Two Pair: there are no pairs in the current cards
            return []
        # p_rem is a list where the highest pair is removed from the current cards
        p_rem = self.removed(p)
        result[:len(p)] = p
        cards = sorted(p_rem) 
        card_len = len(cards)
        i = len(Card.ranks)
        while i > 0:
            same_rank = 0
            for j in range(card_len):
                if i == cards[j].rank:
                    result[same_rank+2] = cards[j]
                    same_rank = same_rank+1
                    # two pair is achieved
                    if same_rank == 2:
                        return result
            i = i - 1
        # failure in detecting a two pair
        result = []
        return result

    def getStraight(self):
        cards = sorted(self.cards)
        card_len = len(cards)
        result = [Card(), Card(), Card(), Card(), Card()]
        cards.reverse()
        ctr = 1
        
        for i in range(len(cards)-1):
            # check if a streak is encountered
            if cards[i].rank - cards[i+1].rank == 1:
                result[ctr-1] = cards[i]
                result[ctr] = cards[i+1]
                ctr = ctr + 1
                if ctr == 5:
                    # streak is 5 straight is achieved
                    return result
            # same rank: do nothing
            elif cards[i].rank - cards[i+1].rank == 0:
                pass
            # reset counter: streak is not encountered
            else:
                ctr = 1
        # failure in detecting a straight: no level 5 streak encountered        
        return []

    def getFlush(self):
        cards = sorted(self.getFlushable())
        if len(cards) < 5:
            return []
        cards.reverse()
        card_len = len(cards)
        result = [Card(), Card(), Card(), Card(), Card()]
        i = len(Card.suits)-1;
        while i >= 0:
            same_suit = 0
            for j in range(card_len):
                if i == cards[j].suit:
                    result[same_suit] = cards[j]
                    same_suit = same_suit + 1
                    if same_suit == 5:
                        # flush is achieved
                        return result
            i = i-1
        # failure in detecting a flush
        return []

    def getStraightFlush(self):
        # f represents a flushable in the current hand
        f = self.getFlushable()
        if len(f) <= 5:
            # no straight flush: current card is not a flushable
            return []
        cards = sorted(f)
        card_len = len(cards)
        result = [Card(), Card(), Card(), Card(), Card()]
        cards.reverse()
        ctr = 1
        for i in range(len(cards)-1):
            # check if a streak is encountered
            if cards[i].rank - cards[i+1].rank == 1:
                result[ctr-1] = cards[i]
                result[ctr] = cards[i+1]
                ctr = ctr + 1
                if ctr == 5:
                    # streak is 5 straight is achieved
                    return result
            # same rank: do nothing
            elif cards[i].rank - cards[i+1].rank == 0:
                pass
            # reset counter: streak is not encountered
            else:
                ctr = 1
        # failure in detecting a straight: no level 5 streak encountered        
        return []
        
        
    # will return the cards that might represent a flush
    def getFlushable(self):
        cards = sorted(self.cards)
        cards.reverse()
        card_len = len(cards)
        # suits contains  a list for the number of cards with the same suit
        suits = [0, 0, 0, 0]
        for i in range(len(Card.suits)):
            for j in range(card_len):
                if i == cards[j].suit:
                    suits[i] = suits[i]+1
        # flushable index
        index = -1
        for i in range(len(suits)):
            # note: only 7 cards in a poker hand :. suit with len >= 5 is flushable
            if suits[i] >= 5:
                index = i
        if index == -1:
            return []
        else:
            result = []
            for i in range(card_len):
                if index == cards[i].suit:
                    result.append(cards[i])
            return result
        # failure in detecting a flushable
        return []
#-------------------------------------------------------------------------------
class Player:
    def __init__(self, money=0, hand = Hand()):
        self.hand = hand
        self.money = money

    def __str__(self):
        return "money: " + self.money.__str__() + "| " + self.hand.getHandType()

    def getHand(self):
        return self.hand
    
    def addCard(self, card):
        self.hand.cards.append(card)

    def addCards(self, cards):
        self.hand.cards.extend(cards)

    def getCards(self):
        return self.hand.cards

    def placeBet(self, bet):
        self.money = self.money - bet
        return bet
#-------------------------------------------------------------------------------
import sys
class Game:
    
    def __init__(self):
        self.round = 0
        self.player = Player(1000, Hand())
        self.comp = Player(999999999999, Hand())
        self.deck = None
        self.deck = Deck()
        self.pot = 0
        self.deck.shuffle()
        input("Deck is ready and shuffled! press enter to continue...")

    def showOption(self):
        print("Enter a number: ")
        print("1 > raise")
        print("2 > fold")
        print("3 > pass")
        self.lnbr()
        try:
            i = int(input("input: "))
            if i == 1:
                return 1
            elif i == 2:
                return 2
            elif i == 3:
                return
            else:
                return self.showOption()
        except ValueError:
            return self.showOption()

    def mainMenu(self):
        print("You are given an initial money of 1000")
        print("Enter a number: ")
        print("1 > start game")
        print("2 > quit")
        self.lnbr()
        try:
            i = int(input("input: "))
            if i == 1:
                self.player.money = 1000
                self.round = 1
                self.startRound(self.round)
            elif i == 2:
                exit(0)
            else:
                return self.mainMenu()
        except ValueError:
            return self.mainMenu()

    def endRoundMenu(self):
        print("Enter a number: ")
        print("1 > next round")
        print("2 > main menu")
        self.lnbr()
        try:
            i = int(input("input: "))
            if i == 1:
                self.lnbr()
                return
            elif i == 2:
                input("back to main menu...")
                self.mainMenu()
            else:
                return self.endRoundMenu()
        except ValueError:
            return self.endRoundMenu()

    def raiseBet(self):
        try:
            i = int(input("amount to raise: "))
            return i
        except ValueError:
            return self.showOption()

    # draw cards
    def drawCard(self):
        return self.deck.popCard()

    def placeBet(self):
        if self.player.money == 0:
            print("Called!")
            return
        c = self.showOption()
        if c == 1:
            bet = self.raiseBet()
            if bet > self.player.money:
                print("Invalid amount!!!")
                self.placeBet()
            else:
                bet = self.player.money - (self.player.money-bet)
                self.player.money = self.player.money - bet
                self.pot = bet + bet
        elif c == 2:
            print("you folded get ready for the next round...")
            input("press enter...")
            self.lnbr()
            self.round = self.round + 1
            self.startRound(self.round)
        else:
            pass
    
    def match(self):
        self.player.hand.getHandType()
        self.comp.hand.getHandType()
        if self.player.hand.type > self.comp.hand.type:
            self.player.money = self.player.money + self.pot
            print("YOU WIN!!!!!!!")
        elif self.player.hand.type == self.comp.hand.type:
            playerCard = self.player.hand.cards
            compCard = self.comp.hand.cards
            if playerCard[0].rank > compCard[0].rank:
                self.player.money = self.player.money + self.pot
                print("YOU WIN!!!!!!!")
            elif self.player.hand.cards[0].rank == self.comp.hand.cards[0].rank:
                self.comp.money = self.comp.money + self.pot/2
                self.player.money = self.player.money + self.pot/2
                print("IT IS A TIE!")
            else:
                self.comp.money = self.comp.money + self.pot
                print("YOU LOSE...")
        else:
            print("YOU LOSE...")
        self.showHand()
        self.showHand("comp")        
        input("press enter to continue...")  
    
    # start round
    def startRound(self, num):
        self.deal()
        self.placeBet()
        self.flop()        
        self.placeBet()
        self.theTurn()
        self.placeBet()
        self.river()
        self.placeBet()
        self.match()
        self.round = self.round + 1
        if self.player.money < 1:
            print("You are bankrupt!")
            input("press enter to return to main menu...")
            self.mainMenu()        
        self.endRoundMenu()
        self.startRound(self.round)

    def flop(self):
        input("The flop! press enter to continue...")
        flop = [self.drawCard(), self.drawCard(), self.drawCard()]
        flop.sort()
        print(flop)
        self.player.addCards(flop)
        self.comp.addCards(flop)
        self.showHand()

    def theTurn(self):        
        input("The turn! press enter to continue...")
        turn = [self.drawCard()]
        turn.sort()
        print(turn)
        self.player.addCards(turn)
        self.comp.addCards(turn)
        self.showHand()

    def river(self):        
        input("The river! press enter to continue...")
        river = [self.drawCard()]
        river.sort()
        print(river)
        self.player.addCards(river)
        self.comp.addCards(river)
        self.showHand()
        
    def deal(self):
        self.player.hand = Hand()
        self.comp.hand = Hand()
        self.player.addCards([self.drawCard(), self.drawCard()])
        self.comp.addCards([self.drawCard(), self.drawCard()])
        self.showHand()
        
    # shows the hand of the specified player default "player")
    def showHand(self, player="player"):
        if player == "player":
            print("YOUR HAND: ", self.player.getCards())
            print("CURRENT STAT--> ", self.player)
        elif player == "comp":
            print("COMP HAND: ", self.comp.hand.getHandType())
        self.lnbr()

    def lnbr(self):
        print("-----------------------------------------------------------------------------")
    
    def start(self):
        self.mainMenu()
#-------------------------------------------------------------------------------
# start the game
Game().start()
#-------------------------------------------------------------------------------
