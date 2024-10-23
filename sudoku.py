"""
CS 021 Final Project
Sudoku Game
Lindsay Hall and James Cilwik
"""


import random
import copy
import sys
import pandas as pd
import time


VALID_BOARDS = [[[1, 2, 4, 5, 6, 3, 7, 8, 9], #TODO constant spacing
                [6, 3, 8, 1, 7, 9, 2, 4, 5],
                [7, 5, 9, 2, 4, 8, 1, 6, 3],
                [4, 8, 6, 9, 1, 2, 3, 5, 7],
                [5, 1, 7, 8, 3, 4, 9, 2, 6],
                [3, 9, 2, 7, 5, 6, 8, 1, 4],
                [9, 7, 1, 6, 2, 5, 4, 3, 8],
                [8, 6, 3, 4, 9, 1, 5, 7, 2],
                [2, 4, 5, 3, 8, 7, 6, 9, 1]],
                
                [[1, 5, 2, 3, 4, 6, 7, 8, 9],
                 [8, 7, 9, 5, 1, 2, 3, 4, 6],
                 [3, 4, 6, 9, 7, 8, 1, 5, 2],
                 [5, 2, 1, 6, 3, 7, 4, 9, 8],
                 [4, 9, 3, 2, 8, 1, 5, 6, 7],
                 [6, 8, 7, 4, 5, 9, 2, 3, 1],
                 [9, 1, 5, 8, 2, 3, 6, 7, 4],
                 [7, 6, 4, 1, 9, 5, 8, 2, 3],
                 [2, 3, 8, 7, 6, 4, 9, 1, 5]],

                [[1, 7, 9, 8, 4, 6, 3, 2, 5],
                 [5, 4, 2, 1, 3, 9, 8, 7, 6],
                 [8, 6, 3, 5, 2, 7, 9, 4, 1],
                 [3, 8, 4, 6, 1, 2, 5, 9, 7],
                 [6, 1, 7, 9, 5, 3, 2, 8, 4],
                 [2, 9, 5, 4, 7, 8, 1, 6, 3],
                 [9, 5, 6, 7, 8, 1, 4, 3, 2],
                 [4, 2, 8, 3, 6, 5, 7, 1, 9],
                 [7, 3, 1, 2, 9, 4, 6, 5, 8]],
                
                [[1, 8, 5, 3, 2, 7, 6, 9, 4],
                 [6, 7, 4, 5, 8, 9, 2, 1, 3],
                 [2, 9, 3, 4, 6, 1, 8, 7, 5],
                 [4, 6, 2, 9, 1, 5, 7, 3, 8],
                 [8, 3, 9, 6, 7, 4, 5, 2, 1],
                 [7, 5, 1, 2, 3, 8, 4, 6, 9],
                 [3, 4, 8, 7, 9, 6, 1, 5, 2],
                 [5, 2, 7, 1, 4, 3, 9, 8, 6],
                 [9, 1, 6, 8, 5, 2, 3, 4, 7]]]
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8]
INPUTS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
LETTERS = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7,
           'h' : 8, 'i' : 9}


def change_board(board, n):
    lst = copy.deepcopy(board)
    c = 0
    while c < n:
        z = random.choice(NUMBERS)
        y = random.choice(NUMBERS)
        x = lst[y][z]
        if x == 0:
            c = c
        else:
            lst[y][z] = 0 
            c += 1
    return lst


def check_numbers(board, b, r, c, z):
    if b[r - 1][c - 1] != 0:
        x = "\n\033[1m\033[31mPlease pick an empty spot to guess\033[0m"
        return x
    elif board[r - 1][c - 1] == z:
        return True
    else:
        return False


def change_numbers(b, r, c, z):
    b[r - 1][c - 1] = z
    return b


if __name__ == "__main__":
    Input = 'yes'
    print('Welcome to our sudoku game!\n'
          'You have \033[1m3 strikes\033[0m. '
          'If you guess the wrong number three times, you lose.\n'
          'The zeros represent empty spaces.\n'
          'Good luck!!\n'
          '- Lindsay and James\n')
    win_count = 0
    while Input.lower() == 'yes' or Input.lower() == 'y':
        start_time = time.time()
        board = random.choice(VALID_BOARDS)
        x = input('Choose your difficulty level '
                  '(easy - 1, medium - 2, hard - 3) or q to quit: ')
        while True:
            if x == '1':
                n = 45 # change this from 45 to 1 to test board faster
                break
            elif x == '2':
                n = 51
                break
            elif x == '3':
                n = 63
                break
            elif x.lower() == 'q':
                print('\nThank you for playing :)')
                sys.exit()
            x = input('\033[1m\033[31mPlease enter 1, 2, or 3 to choose '
                      'your level: \033[0m')
        b = change_board(board, n)
        b2 = pd.DataFrame(b, columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
                          'h','i'], index = ['a', 'b', 'c', 'd','e', 'f', 
                          'g', 'h', 'i'])
        print('\n\033[1mCurrent Board:\033[0m')
        print(b2)
        print(' ')
        w = 0
        while any(0 in row for row in b):
            if w == 3:
                print('\033[1m\033[31mYou lose.\033[0m')
                break
            r = input('Enter the row you want to change or r to '
                      'start a new game or q to quit: ')
            if r.lower() == 'r':
                break
            elif r.lower() == 'q':
                print('\nThank you for playing :)')
                sys.exit()
            else: 
                while r not in LETTERS:
                    print('\033[1m\033[31mPlease enter a letter a-i\033[0m')
                    r = input('Enter the row you want to change or r to '
                              'start a new game: ')
                    if r.lower() == 'r':
                        break
                if r.lower() == 'r':
                    break
                r = LETTERS[r]
            c = input('Enter the column you want to change or q to quit: ')
            if c == 'q':
                print('\nThank you for playing :)')
                sys.exit()
            else:
                while c not in LETTERS:
                    print('\033[1m\033[31mPlease enter a letter a-i\033[0m')
                    c = input('Enter the column you want to change: ')
                c = LETTERS[c]
            while True:
                try: 
                    z = input('Enter the number you want to guess or q to '
                              'quit: ')
                    if z.lower() == 'q':
                        print('\nThank you for playing :)')
                        sys.exit()
                    else:
                        z = int(z)
                    if z in INPUTS:
                        break
                    else:
                        print('\033[1m\033[31mPlease enter a number 1-9'
                              '\033[0m')
                except ValueError:
                    print('\033[1m\033[31mPlease enter a valid number'
                          '\033[0m')
            if check_numbers(board, b, r, c, z) == True:
                print("\n\033[1m\033[32mCorrect! \033[0m")
                b = change_numbers(b, r, c, z)
                b2 = pd.DataFrame(b, columns=['a', 'b', 'c', 'd', 'e', 'f',
                                  'g', 'h', 'i'], index=['a', 'b', 'c', 'd',
                                  'e', 'f', 'g', 'h', 'i'])
                print('\n\033[1mCurrent Board:\033[0m')
                print(b2)
                print(' ')
            elif check_numbers(board, b, r, c, z) == False:
                print(f'\n\033[1m\033[31mIncorrect, you have {2 - w} '
                      'strikes left\033[0m')
                w += 1
                b2 = pd.DataFrame(b, columns=['a', 'b', 'c', 'd', 'e', 'f',
                                  'g', 'h', 'i'], index=['a', 'b', 'c', 'd',
                                  'e', 'f', 'g', 'h', 'i'])
                print('\n\033[1mCurrent Board:\033[0m')
                print(b2)
                print(' ')
            else:
                print(check_numbers(board, b, r, c, z))
                b2 = pd.DataFrame(b, columns=['a', 'b', 'c', 'd', 'e', 'f',
                                  'g', 'h', 'i'], index=['a', 'b', 'c', 'd'
                                  ,'e', 'f', 'g', 'h', 'i'])
                print('\n\033[1mCurrent Board:\033[0m')
                print(b2)
                print(' ')
        if w != 3 and not any(0 in row for row in b):
            print(("\033[2m\033[4m\033[1m\033[31mB\033[91mo"
                   "\033[33ma\033[32mr\033[36md \033[94mi\033[35ms "
                   "\033[31mc\033[91mo\033[33mm"
                   "\033[32mp\033[36ml\033[94mete"
                   "\033[35m!\033[31m Y\033[91mou \033[33mW"
                   "\033[32min\033[36m!\033[4m\033[0m\033[0m"))
            win_count += 1
            end_time = time.time()
            elapsed = end_time - start_time
            print(f'\nIt took you \033[1m{elapsed:.2f}\033[0m seconds to '
                  'complete the game!')
        print(f'\nWin Count = {win_count}')
        Input = input('\nIf you would like to continue, input Y or Yes. '
                      'Input anything else to quit: ')
        print(' ')
        if Input.lower() != 'y' and Input.lower() != 'yes': 
            print('Thank you for playing :)')
            sys.exit()
