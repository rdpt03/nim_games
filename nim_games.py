#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux  de Nim (variante simple et de Marienbad)
"""
if __name__ == '__main__':
    #game vars
    matchsticks = 21
    last_amount_to_remove = 0
    #ask player details
    player1 = input("Insert player 1 name ('ordinateur' to play against the computer): ")
    player2 = input("Insert player 2 name ('ordinateur' to play against the computer): ")

    #check if both players have the same name
    #if player1 == player2:
    #    print("both players cannot have the same name")
    #    exit()
    players = [{'player_n':1, 'name':player1},{'player_n':2,'name':player2}]

    turn = 1
    game_over = False
    #game
    while not game_over:
        #play player 1 or 2
        for player in players:#[1,2]:
            while True:
                #printing area
                print('-'*30)
                print(f"{player['name']}'s turn")
                print(f"{matchsticks} matchsticks remaining in the game")

                #amount to remove (if computer is diferent)
                #computer as player 1
                if player['name'].lower() == 'ordinateur' and player['player_n'] == 1 and turn == 1:
                    amount_to_remove = str(matchsticks % 5)
                    print(f'-> Computer removed {amount_to_remove} matchsticks')
                #computer as player 2
                elif player['name'].lower() == 'ordinateur' and (player['player_n'] == 2 or not turn == 1):
                    amount_to_remove = str(5 - last_amount_to_remove)
                    print(f'-> Computer removed {amount_to_remove} matchsticks')
                #regular player
                else:
                    amount_to_remove = input("Insert the amount of matchsticks to remove (1-4): ")

                turn +=1
                #check if amount is a digit
                if amount_to_remove.isdigit():
                    amount_to_remove = int(amount_to_remove)

                    if 1 <= amount_to_remove <= 4:
                        # remove matchsticks
                        matchsticks -= amount_to_remove
                        last_amount_to_remove = amount_to_remove

                        # check if last was removed
                        if matchsticks <= 0:
                            print(f"{player['name']} (player {player['player_n']}) took the last matchstick and lost the game 😢")
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