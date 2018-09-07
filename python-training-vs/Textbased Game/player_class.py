class Player(object):
    """Player Class"""
    
    def __init__(health, attack, money, level, exp):
        self.maxHealth = health
        self.currentHealth = self.maxHealth
        self.attack = attack
        self.money = money
        self.level = level
        self.exp = exp

    def addExperience(exp):
        self.exp = self.exp + exp
        determineLevel(self.exp)

    def addMoney(amount):
        self.money = self.money + amount

    def removeMoney(amount):
        self.money = self.money - amount
        
    def addHealth(amount):
        currentHp = self.currentHealth + amount
        if currentHp > self.maxHealth:
            self.currentHealth = self.MaxHealth
        else:
            self.currentHealth = currentHp

    def removeHealth(amount):
        currentHp = self.currentHealth - amount
        if currentHp <= 0:
            print("YOU DIED")
        else:
            self.currentHealth = currentHp

    def increaseMaxHealth(health):
        self.maxHealth = self.maxHealth + health

    def determineLevel(exp):
        if exp > 50:
            self.level = self.level + 1