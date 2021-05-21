import os
import numpy as np

clear = lambda: os.system('clear')

def play(players):
    


def selection():
    clear()
    num = int(input("Number of players? (1/2): "))
    assert num in [1,2], "You have to choose between 1 or 2"
    return int(num)

def begin():
    clear()
    print(f"""
    Welcome to TicTacToe 
    
      \/   |       |
      /\   |       |
    -------|-------|-------         
           |   \/  |
           |   /\  |
    -------|-------|--------
      ---  |  ---  |
     |   | | |   | |
      ---  |  ---  |

    Press enter to star ...
    """)
    input()

    players = selection()
    play(players)



def run():
    clear()
    begin()


if __name__ == '__main__':
    run()