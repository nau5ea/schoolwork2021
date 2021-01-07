"""
Author username: Jon Na
Date: 10/5/2020
Assignment/program number: P7
Assignment/program title: Playing Pig
"""

import random

def roll_die(i):
    return random.randint(1,i)

roll_die(6)
    
def take_turn():
    turn_point=0
    keep_rolling=True
    while keep_rolling==True:
        roll=roll_die(6)
        print("You rolled a "+str(roll)+".")
        if roll==1:
            turn_point=0
            keep_rolling=False
        else:
            turn_point+=roll
            print("You now have "+str(turn_point)+".")
            again=input("Roll again? ")
            if "yes"==again:
                keep_rolling=True
            elif "Yes"==again:
                keep_rolling=True
            elif "Y"==again:
                keep_rolling=True
            elif "y"==again:
                keep_rolling=True
            elif "YES"==again:
                keep_rolling=True    
            else:
                keep_rolling=False
                print("Turn over. Sorry :(")
                return turn_point
            
def show_instructions():
    print("Welcome to the Game of Pig. To win, be the player with the most points at the end of the game. The game ends at the end of a round where at least one player has 100 or more points.")
    print()
    print("On each turn, you may roll the die as many times as you like to obtain more points. However, if you roll a 1, your turn is over, and you do not obtain any points that turn.")
    
def play_game():
    total_pointp1=0
    total_pointp2=0
    Player1_name=input("Player 1 name: ")
    Player2_name=input("Player 2 name: ")
    while total_pointp1<100 and total_pointp2<100:
        print("------------------------------------------------")
        print(str(Player1_name)+" has "+str(total_pointp1)+" points. "+str(Player2_name)+" has "+str(total_pointp2)+" points.")
        print("------------------------------------------------")
        input("Your move, "+str(Player1_name)+".")
        total_pointp1=total_pointp1+take_turn()
        print("------------------------------------------------")
        print(str(Player1_name)+" has "+str(total_pointp1)+" points. "+str(Player2_name)+" has "+str(total_pointp2)+" points.")
        input("Your move, "+str(Player2_name)+".")
        total_pointp2=total_pointp2+take_turn()
        if total_pointp1>total_pointp2:
            print(str(Player1_name)+" wins. Congratulations!")
        elif total_pointp1<total_pointp2:
            print(str(Player2_name)+" wins. Congratulations!")
        else: 
            print("Sorry. It was a tie.")
        
def main():
    show_instructions()
    play_game()

main()
    
