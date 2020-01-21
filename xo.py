# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 01:18:17 2020

@author: amrso
"""
import random;

board = ['*','*','*','*','*','*','*','*','*']
player_name = 'player'
next_player = 0
player_sym = ''

def drw_board():
    global board
    print(' ------------')
    for i in range(0,9,3):
        txt =""
        for x in range(3):
            txt += ' | ' + board[i+x].replace('*',str(i+x+1))
        print(txt + ' |')
        print(' ------------')

def is_winer():
    global board
    winer_pttern = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[0,3,6],[1,4,7],[2,5,8],[2,4,6]]
    for i in winer_pttern:
        if (board[i[0]] == '*' or board[i[1]] == '*' or board[i[2]] == '*'):
            continue
        
        elif(board[i[0]] == board[i[1]] == board[i[2]]):
            return True
            
        
        
def get_next_player(last_player):
    if(last_player == 1):
        return 0
    else:
        return 1

def check_board():
    global board
    return board.count('*')


def omputer_next_move():
    
    num = random.randint(1,9)
    while(board[num-1] != '*'):
        num = random.randint(1,9)
    print('Computer play ..  put {} on target {}'.format(player_sym,str(num)))
    return num


def next_move():
    global next_player
    
    if(check_board()):
        if (next_player == 1):
            user_next_try = 0
            while(user_next_try not in range(1,10)):             
                user_next_try = int(input('Your target must be between 1 and 9 : '))
            move(user_next_try)
        else:
            move(omputer_next_move())
    else:
        print('Game over , Board is full')


def move(nxt):
    global board,player_sym,player_name,next_player
    if(board[nxt-1] != '*'):
        print('your target %s already equipped , please try another one' %(nxt))
        next_move()
    else:
        board[nxt-1] = player_sym
        if(player_sym == 'O'): 
            player_sym = 'X'
        else:
            player_sym = 'O'
            
        if(is_winer()):
            if(next_player != 1):
                player_name = 'Computer' 
            print('Winer .. Winer .. Winer .. %s is winer' %(player_name))
            drw_board()

        else:
            drw_board()
            next_player = get_next_player(next_player)
            next_move()


def first_player():
    global next_player
    start = ""
    while (start not in ('Y','N')):
        start = input('if you need to start the game , please enter Y , if you need to computer to be first player enter N : ').upper()
    if(start == 'Y'):
        next_player = 1
    else:
        next_player = 0
        
    next_move()
        
def start_game():
    global player_name
    global player_sym
    print('Welcome to x o Game , please Enter your name to start the game')
    player_name = input("Your name  : ")
    if(player_name != ''):
        print("Welcome %s , let's start the game " %(player_name.upper()))
        while(player_sym.upper() not in ('X','O')):
            player_sym = input("You need to play by X or O  : ").upper()
            if(player_sym in ('X','O')):
                print('Grate your symbol is %s Lest\'s start ..' %(player_sym))
            else:
                print('You enter woring symbol , please try again')
            
            
        first_player()
        

start_game()
