# This class creates a single card of a deck. For simplicity, assume that Ace has a value of 1
# and has the lowest value. King has a value of 13 and has the highest value.
# Order of suits are clubs, spades, hearts and diamonds in ascending order

class Card:
    suits = ["Clubs", "Spades","Hearts","Diamonds"]
    ranks = ["null", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])    
    
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
    
class Hand:
    types = ["high_card", "pair", "two_pair", "trio", "straight", "flush",
             "full", "quad", "straight_flush"]
    
    def __init__(self, card_list):
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
        return self.types[self.type]

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
