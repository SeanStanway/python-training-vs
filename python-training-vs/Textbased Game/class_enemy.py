class Enemy(object):
    """Enemy class"""

    def __init__(name, health, attack, experienceGiven):
        self._name = name
        self._maxHealth = health
        self._currentHealth = self._maxHealth
        self._attack = attack
        self._experienceGiven = experienceGiven
                
        @property
        def name(self):
            return self._name

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
        def experienceGiven(self):
            return self._experienceGiven
        
    def removeHealth(amount):
        currentHp = self._currentHealth - amount
        if currentHp <= 0:
            print("{} has been destroyed!".format(self.name))
        else:
            self._currentHealth = currentHp
            print("{} health lost!".format(amount))

    def reduceAttack(amount):
        newAttack = self._attack - amount
        if newAttack < 0:
            self._attack = 0
        else:
            self._attack = newAttack
