############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

########################## OUR PROGRAM ########################
import random
from art import logo


# print(logo)

# No jokers
# King | Queen | Jack = 10
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
needed_cards = 2
user = []
computer = []

def deal_cards(cards):
    print("giving both players two cards \n\n")
    for i in range(needed_cards):
        user.append(random.choice(cards))
        computer.append(random.choice(cards))
    print(user)
    print(computer)

deal_cards(cards)