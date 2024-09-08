import random

def calscore(cards):
    """
    Calculate the score of the hand.

    Parameters:
    cards (list): A list of integers representing the cards in the hand.

    Returns:
    int: The score of the hand.
    """
    score = sum(cards)
    
    #Special case for Blackjack
    if (score == 21 and len(cards) == 2):
        score = 0  #Represents a Blackjack
    
    #Adjust score if there are Aces and the score is over 21
    if (11 in cards and score > 21):
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
        
    return score
    
def winner(userscore, pcscore):
    """
    Determine the winner based on the scores of the player and the dealer.

    Parameters:
    userscore (int): The score of the player's hand.
    pcscore (int): The score of the dealer's hand.
    """
    if (userscore == pcscore):
        print("It's a Draw!")
    elif (pcscore == 0):
        print("Dealer has Blackjack, you lose.")
    elif (userscore == 0):
        print("You have Blackjack, you win!")
    elif (userscore > 21):
        print("Your score is over 21. You lose.")
    elif (pcscore > 21):
        print(f"Dealer's score is {pcscore}, which is over 21. You win!")
    elif (userscore > pcscore):
        print("You win!")
    else:
        print("You lose.")

print("Let's play Blackjack!\n")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Deal two cards to the player
user = [random.choice(cards) for _ in range(2)]

#Deal two cards to the dealer
pc = [random.choice(cards) for _ in range(2)]

game = True

while game:
    
    userscore = calscore(user)
    print(f"Your cards: {user}, current score: {userscore}")
    
    
    pcscore = calscore(pc)
    print(f"Dealer's first card: {pc[0]}, dealer's score: ?")

    #Check for Blackjack or bust
    if (userscore == 0 or pcscore == 0 or userscore > 21):
        game = False
    else:
        #Player decides whether to draw another card or pass
        user_deal = input("Type 'y' to get a new card, type 'n' to pass: ").lower()
        if user_deal == "y":
            user.append(random.choice(cards))
        else:
            game = False

#Dealer's turn to draw cards
while (pcscore != 0 and pcscore < 17):
    pc.append(random.choice(cards))
    pcscore = calscore(pc)

#Display final hands and scores
print(f"Final hand: Your cards: {user}, your score: {userscore}")
print(f"Final hand: Dealer's cards: {pc}, dealer's score: {pcscore}")

# Determine and announce the winner
winner(userscore, pcscore)
