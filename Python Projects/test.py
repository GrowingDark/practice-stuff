test
import random
import time

class Player(object):
    def __init__(self):
        player_health = 25

    def playerAttack(weaponDamage):
        return weaponDamage

class Weapon(object):
    def __init__(self):
        pass

class Dagger(Weapon):
    def __init__(self):
        self.damage = 5

class Enemy(Player):
    def __init__(self):
        damage = random.randint(0,12)
        self.health = 15

    def enemyDeath(self):
        return "You have slain the beast!"

player = Player()
dagger = Dagger()
enemy = Enemy()
print("You have come across an enemy spider.")
choice = input("Would you like to attack? (Y/N): ")

if choice.upper() == 'Y':

    while enemy.health > 0:

        currentHit = 5
        print("You have dealt " + str(currentHit) + " damage!\n")
        enemy.health -= currentHit
        time.sleep(2)
    print(enemy.enemyDeath())
    input("Press space to continue")
