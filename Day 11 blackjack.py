import random

def add(numl):
    score=0
    for i in range(0,len(numl)):
        score=score+numl[i]
    return score
        

print("lets play blackjack\n")
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
user=[0,0]
for i in range(0,2):
    user[i]=random.choice(cards)

pc=[0,0]
for i in range(0,2):
    pc[i]=random.choice(cards)

userscore=add(user)
print(f"Your cards: {user},current score: {userscore} \n")

pcscore=add(pc)
print(f"Pc first card: {pc}, pc score: {pcscore} \

if(user==[11,10]):
    print("You have Blackjack you win!")

elif(pc==[11,10]):
    print("Pc have Blackjack you lose!")

#in this level
if(userscore>21):
    if(11 in user):
        user[0]=1
        userscore=add(user)
        if(userscore>21):
            print(f"Your score is{userscore} its more than 21 you lose!")
        else:
            #
    else:
        print(f"Your score is{userscore} its more than 21 you lose!")
else:
    #




#test=input("Type y to get another card or type n to pass")
#print(f"Your final cards: {a},current score:{a} \n")
#print(f"Pc final card: {a},final score:{a}\n")

