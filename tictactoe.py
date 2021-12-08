# Tic Tac Toe

import random

def drawBoard(board):
    """(list) -> None

    Function prints out the contents of "board" which is a list of 10 strings, ignoring the value at index 0, in a the a board configuration

        >>>drawBoard("","","X","O","","X","","O","","X","X"])
         |X|X
        -+-+-
        X| |O
        -+-+-
        X|O|
        [KR]
    """
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    # L.S. This function also prints out a prompt for the player to select their letter. 
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose the player who goes first. OA : If 0 the computer goes first. If 1 the player goes first
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

    # L.S. This function has three parameters: board = list with 10 strings, letter = players letter (X or O), move = place on noard (integer from 1 to 9)
def makeMove(board, letter, move):
    # L.S. This code actually passes a reference to the list and not the list itself
   board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    # L.S. This function determines if the player has won by checking every possibility of a tic-tac-toe victory
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    # Make a copy of the board list and return it.
    # L.S. This function is to help the AI when it will sometimes need to make modifications to a temporary copy of the board without changing the actual board. 
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    # L.S. This function essentially checks if a given possible move is available on the board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in their move. When the player types he's move he's letter will show in the space he typed in
    # L.S. This function lets the player enter a number for the space they want on the board. 
    # L.S. We have modified what the printed message is. 
    move = ' '
    # L.S. This loop makes sure the execution doesnt continue until the player enters a number between 1 and 9.
    # L.S. The loop also checks if the move selected is available on the board. 
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    # L.S. This part simply returns the integer form of the move the player entered. 
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    # L.S. This function creates a list of possible moves by checking if theres an available spot on the board. 
    possibleMoves = []
    # L.S. This loop creates the list by using the isSpaceFree function and if it returns true, the move is added to the possibleMoves. 
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    # L.S. This section returns None if there are no possible moves. 
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    """ 
    OA :
    1. Check if we can win in the next move. If yes, place the letter in the wining space. If no continue to the nect step
    2. Check if the player can win in his turn. If yes, try to block the space for the player. If no move to the next step
    3. Focus on the untaken corner's
    4. Focus on the centre if untaken
    5. Focus on the untaken side's 
    """                     
    # First, check if we can win in the next move
    for i in range(1, 10):  # OA: Check all the spaces on the board
        boardCopy = getBoardCopy(board) # OA : Make a copy of the board
        if isSpaceFree(boardCopy, i): # OA : Look for free spaces
            makeMove(boardCopy, computerLetter, i)  
            if isWinner(boardCopy, computerLetter):  # OA : If we can win, place the letter in the winning space
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):   #  OA : Check all the spaces on the board
        boardCopy = getBoardCopy(board) # OA : Make a copy of the board
        if isSpaceFree(boardCopy, i):  # OA : Look for free spaces
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):   # OA : If the player can win, try to block the space that's needed for him to win
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])  # OA : Randomly choose one of the corner
    if move != None: # OA : If the space is not taken
        return move  # OA : Move to that space

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5): #  OA : If the centre is free, take it. If False ,then None(Skip)
        return 5     

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])   # OA : Randomly choose one of the untaken side spaces of the board   

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    # L.S. This function returns true if isSpaceFree returns false (which means there is an available spot on the board). 
    for i in range(1, 10):  # OA : Check all the spaces on the board
        if isSpaceFree(board, i): # OA : Check if there is any free spaces. 
            return False # If there is no free space in the board return False 
    return True          # Returns True if isSpaceFree returns False



print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    drawBoard(theBoard)
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    # L.S. This code below just keeps track of whether the game is still being played. 
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn.
            # L.S. This loop runs if it is the players turn, if turn == 'player' is false, then it jumps to the computers loop. 
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            
            # L.S. This section determines if the player has won or ended in a tie. It also changes gameIsplaying to false. 
            # L.S. It also prints out messages for winnning or tieing, which we have modified. 
            # L.S. The loop breaks if player wins or the board is full. 
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Congratulations! You are victorious!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'computer'
        
        else:
            # Computer's turn.
            # L.S. This loop is for the computers turn              
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            
            # L.S. This section determines if the computer has won or if the game ended in a tie
            # L.S. It breaks if the computer has won or the board is full. 
            # L.S. It also prints out a message for each event which we have modified
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                #displays the computer's win in the terminal [KR]
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'player'
    
    # Offer the player a rematch and end the code if he chooses not to
    # L.S. This code works by checking if the player inputs a word starting with "y", if it doesnt it breaks. 
    # L.S. Changed the message printed    
    print('Play again... if you dare (yes or no)')                        
    if not input().lower().startswith('y'):
        break