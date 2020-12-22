print('ITS TIME TO PLAY VIRTUAL CRICKET')
a='''1. There are 5 player in your and computer team
2. Everytime you and computer needs to choose an integer from 0 to 6,
 if the choices matches the batting player will given out,
 otherwise both the choices will be counted as the run of batsman 
3. In last who win the game is held the winner  
4. You can see the scoreboard at any point by entering the same
5. While bowling you can enter wide also
'''
print(a)

# to make game more interested uses shall input the no. of overs
no_of_overs=int(input('How many overs game you want to play - '))
total_bowls=no_of_overs*6

# these are list from which computer randomly choose
import random
computer_choice_list_bowl=[0,1,2,3,4,5,6,'wide']
computer_choice_list_bat=[0,1,2,3,4,5,6]


run,extrac,no_of_players,bowlc=0,0,5,0
score_board=[]

# this loop will keep on working untill all the player got out
# or all overs got finished
# this loop will add run and give out if choices are same
while bowlc<total_bowls and no_of_players>0:
    your_choice=input()

    try :
        your_choice=int(your_choice)
    except:
        # this allow you to see scoreboard
        if your_choice == 'scoreboard':
            print(sum(score_board) + run + extrac, '-', 5 - no_of_players)
            print(score_board + [str(run) + '*'])
            print('extra -', extrac)
            print('OVERS -', str(bowlc // 6) + '.' + str(bowlc % 6))
            continue
        else:
            # if you enter wrong value it will not stop the game
            print('WRONG INPUT')
            continue

    # if someone choose more than 6 than it is consider wrong
    # so instead of giving error it will display you missed the ball
    if your_choice not in [0,1,2,3,4,5,6]:
        print('You Missed The Ball ')
        bowlc=bowlc+1
        continue


    computer_choice = random.choice(computer_choice_list_bowl)
    print(computer_choice)

    if computer_choice=='wide':
        extrac = extrac + 1
        run = run + your_choice
    elif your_choice!=computer_choice:
        run = run + your_choice + computer_choice
        bowlc = bowlc + 1
    elif your_choice==computer_choice:
        print('OUT')
        bowlc = bowlc + 1
        if run == 0:
            print('OOPS! GOLDEN DUCK')
        no_of_players = no_of_players - 1
        score_board.append(run)
        run = 0


if no_of_players>0:
    score_board.append(run)
if no_of_players==0:
    print('ALL OUT IN -',str(bowlc//6)+'.'+str(bowlc%6),'OVERS')

# batting summary
target=sum(score_board)+extrac+1
print('TOTAL RUNS -',sum(score_board)+extrac,'-',5-no_of_players)
print('SCOREBOARD -',score_board)
print('EXTRA -',extrac )
print('OVERS -',str(bowlc // 6) + '.' + str(bowlc % 6))
print('TARGET -',target)



#your bowling starts

runc,extra,no_of_playersc,bowl=0,0,5,0
score_boardc=[]

while bowl<total_bowls and no_of_playersc>0:
    your_choice=input()
    try :
        your_choice=int(your_choice)
        if your_choice not in [0,1,2,3,4,5,6]:
            print('WRONG INPUT')
            continue
    except:
        # this allow you to see scoreboard
        if your_choice == 'scoreboard':
            print('RUNS -',sum(score_boardc) + runc + extra, '-', 5 - no_of_playersc)
            print('SCOREBOARD -',score_boardc + [str(runc) + '*'])
            print('EXTRA -', extra)
            print('OVERS -', str(bowl // 6) + '.' + str(bowl % 6))
            print('COMPUTER STILL NEEDS -',target-sum(score_boardc) - runc - extra)
            continue
        elif your_choice == 'wide':
            pass
        else:
            # if you enter wrong value it will not stop the game
            print('WRONG INPUT')
            continue


    computer_choice=random.choice(computer_choice_list_bat)
    print(computer_choice)


    if your_choice=='wide':
        extra=extra+1
        runc = runc + computer_choice
    elif your_choice!=computer_choice:
        runc = runc + your_choice + computer_choice
        bowl = bowl + 1
    elif your_choice==computer_choice:
        print('OUT')
        bowl = bowl + 1
        if runc == 0:
            print('HEY! COMPUTER IS OUT ON GOLDEN DUCK')
        no_of_playersc = no_of_playersc - 1
        score_boardc.append(runc)
        runc = 0
    if (sum(score_boardc)+extra+runc)>target-1:
        break

if no_of_playersc>0:
    score_boardc.append(runc)

# these are final comparison to decide the winner
print('\n')
if (sum(score_boardc)+extra)>target-1:
    print('YOU LOST THE GAME BY -',no_of_playersc,'WICKET')
elif (sum(score_boardc)+extra)==target-1:
    print('MATHE TIED')
else:
    print('YOU WON THE GAME BY -',target-1-sum(score_boardc)-extra,'RUNS')

print('\n')

# match summary

print('MATCH SUMMARY')
print('\n\n')
print('YOUR BATTING STATICS...')
print('TOTAL RUN -',sum(score_board)+extrac,'-',5 - no_of_players)
print('OVERS -',str(bowlc // 6) + '.' + str(bowlc % 6))
print('SCOREBOARD -',score_board)
print('EXTRA -',extrac)

print('\n')
print('COMPUTER BATTING STATICS')
print('TOTAL RUNS -',sum(score_boardc) + extra, '-', 5 - no_of_playersc)
print('OVERS -', str(bowl // 6) + '.' + str(bowl % 6))
print('SCOREBOARD -',score_boardc)
print('EXTRA -', extra)
