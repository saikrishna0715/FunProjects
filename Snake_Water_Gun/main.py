import random
import time
import os

MATRIX = [[0,1,-1],[-1,0,1],[1,-1,0]]

def getStatus(comp,player):
    return MATRIX[player][comp]

computer = snake = 0
player = water = 1
CHANCES = 5
if __name__ == '__main__':
    print('Welcome to Snake , Water and Gun Game...... If you want to quit at any point press \'q\'')
    while CHANCES:
        comp_choice = random.randint(0,2)
        print('I am Choosing ...')
        time.sleep(2)
        print('I have something in Mind :)')
        player_choice = input('Enter your Choice (0 : Snake , 1 : Water , 2 : Gun): ')
        if(player_choice not in ['q','quit','0','1','2']):
            print('Please enter a valid number. If You want to quit. Press \'q\'')
            continue
        if(player_choice == 'q' or CHANCES <= 0):
            break
        CHANCES -= 1
        player_choice = int(player_choice)
        comp_choice = random.randint(0,2)
        print('It is a','Win' if getStatus(comp_choice,player_choice) == 1 else ('Draw' if getStatus(comp_choice,player_choice)==0 else 'Loss'))
        print('You choose :',('Snake' if player_choice ==0 else ('Water' if player_choice ==1 else 'Gun')))
        print('Computer choose :',('Snake' if comp_choice ==0 else ('Water' if comp_choice ==1 else 'Gun')))
        time.sleep(3)
        os.system('cls')
    
    print('Thanks for Playing.... Have a Good Day')