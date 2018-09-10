class Player(object):
    """Player Class"""
    
    def __init__(self, name, health, attack, money, level, exp):
        self._name = name
        self._maxHealth = health
        self._currentHealth = self.maxHealth
        self._attack = attack
        self._money = money
        self._level = level
        self._exp = exp

    def printStatus(self):
        print("Name: {}".format(self._name))
        print("Max HP: {}".format(self._maxHealth))
        print("Current HP: {}".format(self._currentHealth))
        print("Attack: {}".format(self._attack))
        print("Money: {}".format(self._money))
        print("Level: {}".format(self._level))
        print("Experience: {}".format(self._exp))

    @property
    def name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    @property
    def maxHealth(self):
        return self._maxHealth

    @property
    def currentHealth(self):
        return self._currentHealth
      
    @property
    def attack(self):
        return self._attack

    @property
    def money(self):
        return self._money

    @property
    def level(self):
        return self._level

    @property
    def exp(self):
        return self._exp

    def addExperience(amount):
        self._exp = self._exp + amount
        determineLevel()

    def addMoney(amount):
        self._money = self._money + amount

    def removeMoney(amount):
        self._money = self._money - amount
        
    def addHealth(amount):
        currentHp = self._currentHealth + amount
        if currentHp > self._maxHealth:
            self._currentHealth = self._MaxHealth
        else:
            self._currentHealth = currentHp

    def removeHealth(amount):
        currentHp = self._currentHealth - amount
        if currentHp <= 0:
            print("YOU DIED")
        else:
            self._currentHealth = currentHp
            print("{} health lost".format(amount))

    def increaseMaxHealth(amount):
        self._maxHealth = self._maxHealth + amount
        
    def increaseAttack(amount):
        self._attack = self._attack + amount

    def determineLevel():
        if self._exp > 50:
            self._level = self._level + 1
            startNewExpBar(self._exp - 50)
            newHealth = self._level * 3
            increaseMaxHealth(newHealth)
            newAttack = self._level / 3
            increaseAttack(newAttack)
            print("Level up! You are now level {}".format(self._level))

    def startNewExpBar(newExp):
        if newExp < 0:
            self._exp = 0
        else:
            self._exp = newExp