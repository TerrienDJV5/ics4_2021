"""

class Item:
    def __init__(self, name, light, melee, range, damage, healing, armour, uses):
        self.name = name   : str
        self.light = light : bool
        self.melee = melee : bool
        self.range = range : int
        self.damage = damage   : int   # think about it
        self.healing = healing  : bool
        self.armour = armour    : bool
        self.uses = uses        : int

"""

gear = {
    'Knife': "False, True, 10, 4, False, False, -1"

}

names = (
    'Drake',
    'Leonard',
    'Alba',
    'Josie',
    'Simon'
    )


if __name__ == "__main__":
    bob = gear['Knife'].split(', ')
    print( bob, bob[1])
    #a = Item('Knife', gear['Knife'][1])