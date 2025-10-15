#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux  de Nim (variante simple et de Marienbad)
"""
import random


def play_marienbad(players):
    #get game plate
    game_plate = generate_marienbad_game()

    playing = True
    #so during the game
    while playing:
        #for each player turn
        for player in players:
            while True:
                if playing:
                    #Printing area
                    barrier()
                    print(f"{player['name']} turn")
                    print('Game area :')
                    for i,game_plate_line in enumerate(game_plate):
                        print(f"{i} : {' | '*game_plate_line}")


                    #check if play is against robot
                    if player['name'].lower() == 'ordinateur':
                        #get all lines with matchsticks available

                        available_matchsticks_lines = [{'line':i, 'matchsticks':x} for i, x in enumerate(game_plate) if x > 0]

                        #get all greater than 1
                        available_matchsticks_lines_greater_than1 = [{'line': x['line'], 'matchsticks': x['matchsticks']} for x in available_matchsticks_lines if x['matchsticks'] > 1]

                        #remove if more the quantity total-1
                        if available_matchsticks_lines_greater_than1:
                            i_to_remove = random.choice([x['line'] for x in available_matchsticks_lines_greater_than1])
                            value_to_remove = game_plate[i_to_remove] - 1

                            game_plate[i_to_remove] -= value_to_remove
                        #if not this available, remove random fron one with 1
                        else:
                            i_to_remove = random.choice([x['line'] for x in available_matchsticks_lines])
                            game_plate[i_to_remove] -= 1

                            if game_plate[i_to_remove] < 0:
                                player['lost_parties'] += 1

                            #check endgame
                        if check_end_game(game_plate, players, playing):
                            playing = False
                        break
                    else:
                        # ask the matchlights to remove and remove
                        line_to_remove = input("-> Insert the line to remove")
                        #check if is a number between given and size
                        if line_to_remove.isdigit() and int(line_to_remove) < len(game_plate) and game_plate[int(line_to_remove)] > 0:
                            #convert to int
                            line_to_remove = int(line_to_remove)

                            #ask and check the amount of matchsticks
                            amount_to_remove = input("-> Insert the amount of matchsticks to remove: ")

                            #check if can remove matchsticks
                            if amount_to_remove.isdigit() and int(amount_to_remove) <= game_plate[line_to_remove]:
                                game_plate[line_to_remove] -= int(amount_to_remove)

                                #handle lost party
                                if game_plate[line_to_remove] <= 0:
                                    print(f"{player['name']} lost one line")
                                    player['lost_parties'] += 1

                                # check endgame
                                if check_end_game(game_plate, players, playing):
                                    playing = False
                                break
                            else:
                                print("[error] You can't remove more than the available match sticks : ")
                        else:
                            print('[error] Insert a correct numerical value for the line to remove : ')


def check_end_game(game_plate : list, players : dict | list, playing : bool):
    if all(x <= 0 for x in game_plate) and playing:
        print("Game finished")
        # find player with most lost parties
        worst_player = max(players, key=lambda p: p['lost_parties'])

        print(f"{worst_player['name']} lost the match")
        return True
    else:
        return False
def generate_marienbad_game():
    playing_sizes = [1, 3, 5, 7]
    random.shuffle(playing_sizes)
    return playing_sizes

def main():
    # game vars
    matchsticks = 21
    last_amount_to_remove = 0
    # ask player details
    player1 = input("Insert player 1 name ('ordinateur' to play against the computer): ")
    player2 = input("Insert player 2 name ('ordinateur' to play against the computer): ")

    # check if both players have the same name
    # if player1 == player2:
    #    print("both players cannot have the same name")
    #    exit()
    players = [{'player_n': 1, 'name': player1, 'lost_parties': 0}, {'player_n': 2, 'name': player2, 'lost_parties': 0}]


    play_marienbad(players)


def barrier():
    """
    Fonction pour créer une barriere de 30 "-"
    """
    print('-' * 30)


if __name__ == '__main__':
    main()