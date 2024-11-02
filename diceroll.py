#generate random dice pairs
import random
class Dice:
    def roll(self):
        s=random.randint(1,6)
        u=random.randint(1,6)
        return(s,u)

obj1=Dice()
print(obj1.roll())