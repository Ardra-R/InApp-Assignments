import random
choices={'rock':1,'paper':2,'scissors':3}
print(choices)
round=0
p=0
c=0
Choices={}
while(round<10):
    player_choice=int(input('enter number corresponding to players choice from given list:'))
    computer_choice=random.choice(list(choices.values()))
    print("Computers choice is:",computer_choice)
    if(player_choice==computer_choice):
        result='tie'
    elif (player_choice-computer_choice) == (-2) or (player_choice-computer_choice) == (1):
        result='player'
        p+=1
    else:
        result='computer'
        c+=1
    Choices[round]=[player_choice,computer_choice,result]
    round+=1
if(p==c):
    print('Its a tie')
elif(p>c):
    print('The winner is player')
    print('Total points earned by player:',p)
    print('Total points earned by computer:',c)
else:
    print('The winner is computer')
    print('Total points earned by player:',p)
    print('Total points earned by computer:',c)

while True :
    r=int(input('enter round  from 0 to 9 for which you need the information:'))
    if 0<=r<10:
        print('players choice:',Choices[r][0])
        print('computers choice:',Choices[r][1])
        if (Choices[r][2]=='tie'): print('Its a tie')
        else: print('Winner is:', Choices[r][2])
    else:
        print('This round does not exist')
        continue
