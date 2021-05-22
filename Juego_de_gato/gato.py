import os

clear = lambda: os.system('clear')

def check(X,X_win):
  if ((X[0] == X_win or X[1] == X_win or X[2] == X_win) or 
    (X[0][0] == 'X' and X[1][1] == 'X' and X[2][2] == 'X') or 
    (X[0][2] == 'X' and X[1][1] == 'X' and X[2][0] == 'X') or
    (X[0][0] == 'X' and X[1][0] == 'X' and X[2][0] == 'X') or 
    (X[0][2] == 'X' and X[1][2] == 'X' and X[2][2] == 'X') or
    (X[0][1] == 'X' and X[1][1] == 'X' and X[2][1] == 'X')):
    return True
  else:
    return False

def row_col():
  x = int(input("Choose a row (1,2,3): "))
  y = int(input("Choose a column (1,2,3): "))
  return [x-1,y-1]

def IA(X):
  clear()
  print("IA's turn...")
  for i in range(len(X)):
    for j in range(len(X)):
      if X[i][j] == ' ':
        X[i][j] = 'O'
        table(X)
        input("Press enter to continue...")
        return


def table(a):
  print(f"""
      1   2   3          

  1   {a[0][0]} | {a[0][1]} | {a[0][2]}          
     -----------
  2   {a[1][0]} | {a[1][1]} | {a[1][2]} 
     -----------
  3   {a[2][0]} | {a[2][1]} | {a[2][2]} 
  
  """)

#####################-----TWO PLAYERS CODE-------#############################
def two():
  clear()
  X = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
  X_win = ['X','X','X']
  O_win = ['O','O','O']
  x_win = False
  o_win = False
  i = -1

  while x_win == False or o_win == False or i == 9:

    i += 1
    if i == 9:
      table(X)
      print("""
      It's a tie
      """)
      ans = input("Play again (y/n): ")
      if ans == 'y':
        two()
      else:
        clear()
        input(''' 
        Goodbye

        Press enter to continue... ''')
        break
    #print(f"i = {i}")

    print("      Player's one turn...")
    table(X)
    coords = row_col()
    X[coords[0]][coords[1]] = 'X'
    #clear()
    x_win = check(X,X_win)
    if x_win == True: 
      clear()
      table(X)
      print(""" 
      Player one wins!!!
      """)
      ans = input("Play again (y/n): ")
      if ans == 'y':
        two()
      else:
        clear()
        input(''' 
        Goodbye
        
        Press enter to continue... ''')
      break

    input("Press enter to continue...")
    clear()

    i += 1
    if i == 9:
      table(X)
      print("""
      It's a tie
      """)
      ans = input("Play again (y/n): ")
      if ans == 'y':
        two()
      else:
        clear()
        input(''' 
        Goodbye

        Press enter to continue... ''')
        break
    #print(f"i = {i}")
    print("      Player's two turn...")
    table(X)
    coords = row_col()
    X[coords[0]][coords[1]] = 'O'
    #clear()
    o_win = check(X,O_win)

    if o_win == True:
      clear()
      table(X)
      ans = input('''
      Player two wins!!!

      Try again (y/n):
      ''')
      if ans == 'y':
        two()
      else:
        clear()
        input(''' 
        Goodbye
        
        Press enter to continue... ''')
      break
    input("Press enter to continue...")
    clear()

    
##--------------------------------------------------------------------------## 

#####################-----ONE PLAYER CODE-------#############################
def one():
  X = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

  X_win = ['X','X','X']
  O_win = ['O','O','O']
  win = False

  while win == False:
    print("Your turn...")
    table(X)
    coords = row_col()
    X[coords[0]][coords[1]] = 'X'
    clear()
    table(X)
    win = check(X,X_win)
    if win == True: 
      clear()
      table(X)
      print(""" 
      You Win!!!
      """)
      ans = input("Play again (y/n): ")
      if ans == 'y':
        run()
      else:
        clear()
        input(''' 
        Goodbye
        
        Press enter to continue... ''')
      break
    input("Press enter to continue...")
    IA(X)
    clear()
    loose = check(X,O_win)
    if loose == True:
      clear()
      table(X)
      ans = input('''
      You loose :(

      Try again (y/n):
      ''')
      if ans == 'y':
        run()
      else:
        clear()
        input(''' 
        Goodbye
        
        Press enter to continue... ''')
      break
##--------------------------------------------------------------------------## 

def play(players):
  if players == 1:
    one()
  elif players == 2:
    two()
    

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

  Press enter to start ...
  """)
  input()

  players = selection()
  play(players)



def run():
  clear()
  begin()


if __name__ == '__main__':
  run()