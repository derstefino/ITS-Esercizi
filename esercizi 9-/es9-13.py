'''9-13. Dice: Make a class Dice with one attribute called sides, which has a default value of 6.
Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.
Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.
'''
import random

class Dice:
    
    def __init__(self, sides=6):

        self.sides=sides

    def roll_die(self):

        print(random.randint(1,self.sides))



dice_six = Dice()

dice_six.roll_die()

dice_ten = Dice(sides=10)

dice_ten.roll_die()

dice_twenty = Dice(sides=20)

dice_twenty.roll_die()