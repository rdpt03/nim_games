#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux  de Nim (variante simple et de Marienbad)
"""
if __name__ == '__main__':
    #game vars
    matchsticks = 21

    #ask player details
    player1 = input("Insert player 1 name : ")
    player2 = input("Insert player 2 name : ")
    players = {1:player1,2:player2}

    game_over = False
    #game
    while not game_over:
        #play player 1 or 2
        for player_num in [1,2]:
            while True:
                #printing area
                print('-'*30)
                print(f"{players[player_num]}'s turn")
                print(f"{matchsticks} matchsticks remaining in the game")

                #amount to remove
                amount_to_remove = input("Insert the amount of matchsticks to remove (1-4): ")

                #check if amount is a digit
                if amount_to_remove.isdigit():
                    amount_to_remove = int(amount_to_remove)

                    if 1 <= amount_to_remove <= 4:
                        # remove matchsticks
                        matchsticks -= amount_to_remove


                        # check if last was removed
                        if matchsticks <= 0:
                            print(f"{players[player_num]} took the last matchstick and lost the game 😢")
                            game_over = True
                            break
                        else:
                            break
                    else:
                        print("Please insert an amount between 1 and 4.")
                else:
                    print("Invalid input. Please enter a number between 1 and 4.")
            if game_over:
                break