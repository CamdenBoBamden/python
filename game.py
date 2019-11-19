# Make a blackjack game in python. There are 2 players in the game: you and the dealer. 
# The dealer deals two cards to you at the start of a hand, and two cards to itself one face 
# up and one face down. You then have an option to "hit" or "stay". Once you have either stayed or 
# busted, the dealer plays. The dealer must hit if their hand is less than or equal to 16 and they must hit otherwise. 
# 
# The entire game is played out by text, for example:
# Start of new hand - dealing:
# You have A,7
# The dealer is showing J
# [H]it or [S]tay: S <-prompt for an action here
# You stay with 18
# Dealer shows J,5
# Dealer hits and draws a Q
# Dealer busts, you win.
# Start of new hand - dealing: ...
# Note: Design the game in terms of object oriented classes with state and behavior.

import random

A = 11
K = 10
Q = 10
J = 10
class Card:
    def __init__(self,name):
        self.hit = name
        cards= [A,K,Q,J,2,3,4,5,6,7,8,9,10]
        self.hit = random.choice(cards)

class MyHand:
    def __init__(self, cardOne, cardTwo, name):
        self.cardOne = cardOne
        self.cardTwo = cardTwo
        self.name = name

    def startingHand(self):
        print(self.name, "at", self.cardOne,"and ",self.cardTwo)
        print(self.name, ' sitting at', self.cardOne+self.cardTwo)
    
    def score(self):
        total = self.cardOne+self.cardTwo 
        
        if total > 21:
            print ("BUST")
        elif total == 21:
            print ("BlackJack!")
        else:
            userChoice = input("Would you like to hit or stay? ")
            
            if userChoice == "stay":
                print("")
                print ("You have chosen to STAY")
            else:
                print("")
                print ("You've chosen to hit")
                print("Here is your next card.")
                nextCard = Card(3)
                hand = MyHand(total, nextCard.hit, "You're")
                hand.startingHand()
                hand.score()


print("")
print('Starting Game')
firstC = Card(1)
secondC = Card(2)
dealerC1 = Card(7)
dealerC2 = Card(8)

dealerHand = MyHand(dealerC1.hit,dealerC2.hit, "Dealer's")
dealerHand.startingHand()

hand = MyHand(firstC.hit,secondC.hit, "You're")

print("")
hand.startingHand()
print("")
hand.score()


