import random
choices=['rock','paper','scissors']
print(choices)
round=0
p=0
c=0
Choices={}
while(round<10):
    player_choice=input('enter player choice from given list:')
    computer_choice=random.choice(choices)
    if(player_choice==computer_choice):
        result='tie'
    elif(player_choice=='rock' and computer_choice=='scissors' ):
        result='player'
    elif(player_choice=='scissors' and computer_choice=='paper'):
        result='player'
    elif(player_choice=='paper' and computer_choice=='rock'):
        result='player'
    else:
        result='computer'
    Choices[round]=[player_choice,computer_choice,result]
    round=round+1
    if(result=='tie'):
        p=p
        c=c
    elif(result=='player'):
        p=p+1
    elif(result=='computer'):
        c=c+1
if(result=='tie'):
    print('Its a tie')
else:
    print('The winner is:',result)
    print('Total points earned by player:',p)
    print('Total points earned by computer:',c)
print(Choices)

