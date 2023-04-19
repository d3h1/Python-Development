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


print(logo)

def deal_card(cards):
    return random.choice(cards)

def player_hand(cards, numOfCards = 2):
    playerCards = [] # Declaring an empty list to fill with the players randomly assorted cards
    for i in range(numOfCards):
        playerCards.append(deal_card(cards))
        # print(playerCards[i])
    
    return playerCards
        
def calculate_hand(cards):
        total_hand = sum(cards)
        if 11 in cards and total_hand > 21:
            total_hand -= 10
        return total_hand

def card_checker(computerScore, userScore):
    if computerScore == 21:
        print('The computer has won the game')
    elif userScore == 21:
        print('The user has won the game')
    elif computerScore > 21:
        print(f'The user has won with {userScore} points!')
    elif userScore > 21:
        print(f'The computer has won with {computerScore} points!')
    elif computerScore > userScore:
        print(f'The computer has won over the user at {computerScore} points!')
    elif userScore > computerScore:
        print(f'The computer has won over the user at {userScore} points!')
    else:
        print(f'Both players have tied at a score of {userScore}')

# Main Function
def play_game(cards):
    computerHand = player_hand(cards)
    userHand = player_hand(cards)
    print(f'The computers first two cards add up to: {sum(computerHand)}')
    print(f'The users first two cards add up to: {sum(userHand)}')
     
    while True:
        draw_card = input('Would you like to add another card to your hand?').lower()
        if draw_card == 'y':
            userHand.append(deal_card(cards))
            print(f'You currently have: {userHand}')
            currentUserScore = calculate_hand(userHand)
            if currentUserScore > 21:
                print(f'You have have reached a bust with a score of: {currentUserScore}')
                card_checker(calculate_hand(computerHand), currentUserScore)
                return
        else:
            break
        
    currentComputerScore = calculate_hand(computerHand)
    while currentComputerScore < 17:
        computerHand.append(deal_card(cards))
        currentComputerScore = calculate_hand(computerHand)
    print(f'Computer Cards: {computerHand}')
    
    currentUserScore = calculate_hand(userHand)
    card_checker(currentComputerScore, currentUserScore)
            
        
    
    
                
             
             

# No jokers
# King | Queen | Jack = 10
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]


play_game(cards)



