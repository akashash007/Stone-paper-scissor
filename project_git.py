# importing random
import random

#Creating rules 
print("Rules----------->\n0 for stone\n1 for paper \n2 for scissor")
print('''    points to win the match
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''
    '''
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    '''

    '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)

    ''')

#instantiating
player_score=0
computer_score=0

#creating while 
while player_score < 3 and computer_score < 3:

    stone='''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
        '''
    paper = '''
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        '''

    scissor='''
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)

        '''
#adding ascii images to list
    asci=[stone,paper,scissor]

#taking input
    player=int(input("enter a number : "))
    print("Hooman: ")


#printing ascii value of users
    x=asci[player]
    print(x)

#creating random list
    computer=(random.randint(0,2))

#creating if statement
    print('computer:')
    if player==0 and computer==2:
        print(asci[computer])
        print('Hooman won')
        player_score+=1
        
    elif computer==0 and player==2:
        print(asci[computer])
        print('computer win')
        computer_score+=1
        
    elif computer > player:
        print(asci[computer])
        print('computer win')
        computer_score+=1
        
    elif player > computer :
        print(asci[computer])
        print('Hooman Win')
        player_score+=1
        
    elif computer == player:
        print(asci[computer])
        print('Its Draw bro')

    elif player >=3 or player<0:
        print('You typed invalid number try again,',player)
print("Final Score: ")
print("Hooman Score:",player_score)
print("Computer Score:",computer_score)

if player_score > computer_score:
    print('Hooman Won the match')
elif player_score < computer_score:
    print('Computer Won the match')
else:
    print("It's Tie")
    
        
        
            
             
