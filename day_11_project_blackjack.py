import random

#fucntion to calculate the score
def calscore(cards):
    score=sum(cards)
    
    #a score for blackjack
    if(score==21 and len(cards)==2):
        score=0
    
    #change the value of the ace from 11 to 1 if if the score is over 21
    if(11 in cards and score>21):
        cards.remove(11)
        cards.append(1)
        score=sum(cards)
        
    return score
    
#fucntion to check the winner
def winner(userscore,pcscore):
    #Draw 
    if(userscore==pcscore):
        print("It's Draw! ")
    
    #Pc blackjack
    elif(pcscore==0):
        print("Pc have blackjack you lose")
    
    #user blackjack
    elif(userscore==0):
        print("You have blackjackm you win")
    
    #User over 21
    elif(userscore>21):
        print("Your score is over 21. You lose ")
        
    #pc over 21
    elif(pcscore>21):
        print(f"Pc score is {pcscore}. It's over 21. You win ")
    
    #User bigger than pc
    elif(userscore>pcscore):
        print("Your win")
    
    #Pc bigger than user
    else:
        print("Your lose")

    
print("lets play blackjack\n")
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

#user get 2 random cards
user=[0,0]
for i in range(0,2):
    user[i]=random.choice(cards)

#pc get 2 random cards
pc=[0,0]
for i in range(0,2):
    pc[i]=random.choice(cards)


game=True

while game:
    #calculate the user score and print the user score with the cards
    userscore=calscore(user)
    print(f"Your cards: {user},current score: {userscore} \n")

    #calculate the pc score and print the pc 1st card
    pcscore=calscore(pc)
    print(f"Pc first card: {pc[0]}, pc score: ? ")

    #check for blackjack
    if(userscore==0 or pcscore==0 userscore>21):
        game=False
    
    #get new card
    user_deal=input("type y to get new card, type n to pass: ")
    if(user_deal=="y"):
        user.append(random.choice(cards))
    else:
        
        game=False

while pcscore+!0 and pcscore<17:
    pc.append(random.choice(cards))
    pcscore=calscore(pc)

print(f"Final hand. Your cards: {user},your score: {userscore} \n")
print(f"Final hand. Pc cards: {pc},pc score: {pcscore} \n")
winner(userscore,pcscore)
