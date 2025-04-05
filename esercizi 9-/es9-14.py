'''9-14. Lottery: Create a class LotteryMachine that holds a list containing a series of 10 numbers and 5 letters.
Implement a method to randomly select 4 items (numbers or letters) from this list to draw a winning ticket.
Finally, implement a method to display a message saying that any ticket matching the winning 4 items wins a prize.
'''
import random

class LotteryMachine:

    def __init__(self, items:list=["4","6","55","89","23","10","1","7","33","34","a","z","v","k","e"]):

        self.items=items

    def extract(self):

        win = [] 
        
        while len(win)<4:
            
            item = self.items[random.randint(0,len(self.items)-1)]
            if item not in win:
                win.append(item)

        return win
    
    def show_winning_items(self):
        
        if len(LotteryMachine().extract())!=0:

            print(f"any ticket matching the following items wins a prize!\n{LotteryMachine().extract()}")



m = LotteryMachine()

m.extract()

m.show_winning_items()
            