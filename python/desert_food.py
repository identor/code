import math

class Food:
    def __init__(self, name, weight, volume, cal):
        self.name = name
        self.weight = weight
        self.volume = volume
        self.cal = cal
        
    def __str__(self):
        return self.name

def tom():
    TOM_MAX = 15.0
    tiny = 0.77
    small = 1.10
    medium = 3.4
    large = 7
    carry_weight = 0
    
    for i in range(0, (math.floor(TOM_MAX/small)+1)):
        print(small*i)
        print((tiny * math.floor(TOM_MAX-(small*i)/tiny)) + small*i)

    '''
    print(tiny * math.floor(TOM_MAX/tiny))
    print(small * math.floor(TOM_MAX/small))
    print(medium * math.floor(TOM_MAX/medium))
    print(large * math.floor(TOM_MAX/large))        
    '''
    
def gina():   
    food_items = []
    food_items.append(Food("Granola Bars", 240, 400, 900))
    food_items.append(Food("Potato Chips", 135, 400, 650))
    food_items.append(Food("Beef Jerky", 2800, 1500, 5000))
    food_items.append(Food("Almonds", 410, 410, 950))
    food_items.append(Food("Apples", 182, 190, 95))    
    for i in food_items:
        print(i)


