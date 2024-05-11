'''
Card game war
split 52 card deck into 2  sub decks one for each player
grab each card from each deck and compare
if higher grab both and add to deck
loses if any player has 0 cards left
if same value.
jack == jack
take additional set of cards and compare and take cards into winning deck (pile of 3 is taken)
'''
import random as r
from datetime import datetime

def writeToScoreboard(rounds, players):
    with open("war_game_scoreboard.txt", "a") as sb:
        datetimestamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S %p")
        sb.write(f"{datetimestamp} : Players {players[0]} VS {players[1]} played {rounds} rounds and the winner is player {players[0]} \n")
    sb.close()
        
suits = ("Hearts","Clubs","Spades","Diamonds")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
number_card_values = {"Two":2,"Three":3, "Four":4, "Five":5, "Six":6, "Seven":7,"Eight":8,"Nine":9,"Ten":10, "Jack": 11,
                      "Queen":12, "King": 13, "Ace": 14}

class Card:
    """
    suit, rank and value 
    """
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = number_card_values[self.rank]
    def __str__(self):
        return f"{self.rank} of {self.suit}"    

class Deck:
    """
    collection of 52 cards i.e. list of Card objects 
    has shuffle method
    has dealcards method
    """
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    def shuffleDeck(self):
        r.shuffle(self.all_cards)
    def dealCards(self, deck):
        player_one_cards = r.sample(deck,26)
        player_two_cards = [x for x in deck if x not in player_one_cards]
        return (player_one_cards, player_two_cards)
    def dealOne(self):
        return self.all_cards.pop()
    def __str__(self):
        card_list = ""
        for card_no,card in enumerate(self.all_cards):
            card_list += f"{card_no+1}. {card}\n" 
        return card_list

class Player:
    """
    player can add or remove cards single / multiple
    player - plays a card from top of card .pop(0) pop at 0th index
    take card from bottom of players card to play
    add card to bottom of card list- append() for single
    add multiple cards to hand - use extend(list of cards)
    """
    def __init__(self,name):
        self.name = name
        self.all_cards = []
        
    def removeOne(self):
        return self.all_cards.pop(0) #removed from the top of card stack
    def add_cards(self, new_cards):
        if type(new_cards) == type([]): #multiple card objects
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards) #single card object
    def __str__(self):
        return f"This is a player {self.name} having {len(self.all_cards)} cards."
    

if __name__ == '__main__':   
    """
    game_on = True until one of the player has no cards remaining.
    while game_on
        while at_war 
            keep drawing cards until tie ends and one player wins
        make false (while_at_war)
        once any player loses game_on=False
    """
    player1 = Player("A")
    player2 = Player("B")
    
    new_deck = Deck()
    new_deck.shuffleDeck()
    
    player1_cards, player2_cards = new_deck.dealCards(new_deck.all_cards)
    player1.add_cards(player1_cards)
    player2.add_cards(player2_cards)
    
    game_on = True
    round_number = 0
    while game_on:
        round_number += 1
        print(f"This is Round {round_number}\n")
        if (len(player1.all_cards) == 0):
            print(f"Player {player1.name} is out of cards...You lose!!!!! The winner is player {player2.name}")
            game_on = False
            break
        if (len(player2.all_cards) == 0):
            print(f"Player {player2.name} is out of cards...You lose!!!!! The winner is player {player1.name}")
            game_on = False
            break
        else:
            #player's current cards  in hand
            player_one_cards = [] 
            player_two_cards = []
            
            player_one_cards.append(player1.removeOne())
            player_two_cards.append(player2.removeOne())
            
            """
            Comapre the cards - less , greater or equal to (war situation)
            draw additional 5 cards when a war situation is there
            lose if not atleast 5 cards in their hand
            need atleast 3 cards to do war
            """
            
            at_war = True
            #draw card from bottom and assuming that there is a stack of cards 
            while at_war:
                if (player_one_cards[-1].value > player_two_cards[-1].value):
                    player1.add_cards(player_one_cards)
                    player1.add_cards(player_two_cards)
                    at_war = False
                elif (player_one_cards[-1].value < player_two_cards[-1].value): 
                    player2.add_cards(player_two_cards)
                    player2.add_cards(player_one_cards)  
                    at_war = False
                else:
                    # at_war = True
                    print("WAR has started...\n")
                    if (len(player1.all_cards) < 3):
                        print("Player 1 cannot declare WAR.\n")
                        print(f"Player {player2.name} wins!!")
                        game_on = False
                        break
                    elif (len(player2.all_cards) < 3):
                        print("Player 2 cannot declare WAR.\n")
                        print(f"Player {player1.name} wins!!")
                        game_on = False
                        break
                    else:
                        print("Drawing 3 extra cards....\n")
                        for i in range(3):
                            player_one_cards.append(player1.removeOne())
                            player_two_cards.append(player2.removeOne())
                            
            if (len(player1.all_cards) == 0): 
                writeToScoreboard(round_number, (player2.name,player1.name))   
                
            elif(len(player2.all_cards) == 0):
                writeToScoreboard(round_number, (player1.name,player2.name))  
                    
                    
                    

            
            
        
    
    
    