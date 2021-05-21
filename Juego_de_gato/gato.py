import os
import numpy as np

clear = lambda: os.system('clear')

def table(a):
  print(f"""
      1   2   3          

  1   {a[0][0]} | {a[0][1]} | {a[0][2]}          
     -----------
  2   {a[1][0]} | {a[1][1]} | {a[1][2]} 
     -----------
  3   {a[2][0]} | {a[2][1]} | {a[2][2]} 
  
  """)

def one():
  print("""
       1   2   3

  1      |    | 
      -------------
  2      |    |  
      -------------
  3      |    |  
  
  """)
  X = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
  row = int(input("Choose a row (1,2,3): "))
  col = int(input("Choose a column (1,2,3): "))
  X[row-1][col-1] = 'X'
  table(X)
  # table = [[0,0,0],[0,0,0],[0,0,0]]
  # win = False
  # while win != True:




def play(players):
  if players == 1:
    one()
    

def selection():
  clear()
  num = int(input("Number of players? (1/2): "))
  assert num in [1,2], "You have to choose between 1 or 2"
  return num

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