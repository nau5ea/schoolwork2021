# -*- coding: utf-8 -*-
"""
This is the second part of the pig game.
"""

def play_game():
    total_points_one = 0
    total_points_two = 0
    while total_points_one < 100 and total_points_two < 100:
        print("Player one has " + str(total_points_one) + " points.","Player one has " + str(total_points_two) + " points.")
        input("Player 1, it is your turn.")
        total_points_one += take_turn()
        print("Player one has " + str(total_points_one) + " points.","Player one has " + str(total_points_two) + " points.")
        input("Player21, it is your turn.")
        total_points_two += take_turn()
        print("Player one has " + str(total_points_one) + " points.","Player one has " + str(total_points_two) + " points.")
    if total_points_one > total_points_two:
        print("The game is over. Player one has triumphed.")
    elif total_points_two > total_points_one:
        print("The game is over. Player two has triumphed.")
    else:
        print("The game ended in a tie.")