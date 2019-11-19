import random
import time

class Card:
    def __init__(self,name):
        self.hit = Deck(1).hit

    
class Dealer:
    def __init__(self,name,dcards):   
        self.name = name
        self.dcards = dcards
        print(self.name, "will now play through.")
        pause()
        print(self.name,"shows both cards now", self.dcards[0], "and", self.dcards[1])  
        pause()
        Hand(self.name, self.dcards)
        
class Player:
    def __init__(self,name,cards):
        self.name = name
        self.cards = cards
        print(self.name, "has", self.cards[0],"and", self.cards[1])
        pause()
        Hand(self.name, self.cards)
        
class Hand:
    def __init__(self,name,cards):
        self.name = name
        self.cards = cards
        total = sum(self.cards)
        print(self.name, "has a total of",total)
        pause()
        #below is the dealer playing their hand through
        if self.name == "Dealer":
            if total > 21:
                pause()
                print ("Dealer BUSTS Player Wins")
            elif total < 17:
                pause()
                print ("Dealer has less than 16 and must hit")
                pause()
                print("Here is the Dealer's next card.")
                pause()
                cards.append(Card(1).hit)
                print(cards)
                pause()
                Hand(self.name,cards)

            elif total == 21:
                pause()
                print ("BlackJack! Dealer Wins!")
            else:
                print ("Dealer ends with", total)
        #Below is the player playing their hand through           
        else:
            if total > 21:
                pause()
                print ("BUST! Dealer Wins")
                print("need to end game here")
            elif total == 21:
                pause()
                print ("BlackJack!")
            else:
                pause()
                userChoice = input("Would you like to hit or stay? ")
                
                if userChoice == "stay":
                    pause()
                    print ("You have chosen to stay.")
                    pause()
                    return 
                  
                else:
                    pause()
                    print ("You've chosen to hit.")
                    pause()
                    print("Here is your next card.")
                    pause()
                    cards.append(Card(1).hit)
                    print(cards)
                    Hand(self.name,cards)
                    

class Deck:
    def __init__(self,name):
        A = 11
        K = 10
        Q = 10
        J = 10
        cards = [A, K, Q, J, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.hit = random.choice(cards)

class Game:
    def __init__(self,name):
        print("Dealer deals 2 cards and 2 to self with one hidden.")
        playerCards = [Card(1).hit, Card(2).hit]
        dealerCards = [Card(1).hit, Card(2).hit]
        pause()
        print("Dealer has", dealerCards[0], "and one face down.")
        pause()
        if dealerCards[0] == 10:
            print("something for insurance")
            pause()
        else:
            pass    

        Player("Cam", playerCards)
        print("Player finished need to save their total to compare to Dealer total at end.")
        pause()
        Dealer("Dealer", dealerCards)
  
class pause:
    def __init__(self):
        time.sleep(1)
        print("")

        
       
Game("New Game")