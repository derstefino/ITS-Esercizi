'''9-15. Lottery Analysis: Extend the LotteryMachine class you created in Exercise 9-14.

1. Add a method called simulate_until_win(self, my_ticket) that:

    Accepts a ticket (a list of 4 items).
    Repeatedly draws random tickets using the draw_ticket() method.
    Keeps count of how many attempts it takes until a randomly drawn ticket matches my_ticket.
    Returns the number of attempts and the winning ticket.

2. Create a ticket called my_ticket with 4 numbers or letters from the pool.

3. Use the simulate_until_win() method to simulate how many draws it would take for your ticket to win.

4. Print a message showing:

    Your ticket
    The winning ticket
    How many attempts it took to win

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

    def simulate_until_win(self, my_ticket:list):
        
        count = 0
        winning_ticket=LotteryMachine().extract()

        while set(my_ticket) != set(winning_ticket):
            
            winning_ticket=LotteryMachine().extract()
            count+=1
            
        
        print(f"Your ticket: {my_ticket}\nThe winning ticket: {winning_ticket}\nHow many attempts it took to win: {count}")



m=LotteryMachine()

m.simulate_until_win(["23","10","1","a"])
