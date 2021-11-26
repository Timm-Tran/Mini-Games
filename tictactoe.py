def game():
    gameBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    gameOver = False
    tie = False
    player = 1
    
    print(f"\n\nWelcome to a game of tictactoe! Player 1 will be 'x' and go first, Player 2 will be 'o' and go second. Good luck!")
    
    while not gameOver:
        showGameBoard(gameBoard)
        move = askPlayerMove(player, gameBoard)
        if player == 1:
            gameBoard[move - 1] = 'x'
            gameOver, tie = checkGameState(gameBoard)
            if gameOver: break
            else: player = 2
        else:
            gameBoard[move - 1] = 'o'
            gameOver, tie = checkGameState(gameBoard)
            if gameOver: break
            else: player = 1
    
    if not tie:
        print(f'\n\nCongradulations! Player {player} has won the game!')
    else:
        print(f'\n\nStalemate!')
    showGameBoard(gameBoard)

def showGameBoard(gameBoard):    
    print(f'\n\n\t\t    Current Game Board')
    print(f'\t\t\t {gameBoard[0]} | {gameBoard[1]} | {gameBoard[2]} \n\t\t\t {gameBoard[3]} | {gameBoard[4]} | {gameBoard[5]} \n\t\t\t {gameBoard[6]} | {gameBoard[7]} | {gameBoard[8]}')

def askPlayerMove(player, gameBoard):
    response = False
    print(f'\nPlayer {player} please pick a spot 1-9')
    print(f' 1 | 2 | 3 \n 4 | 5 | 6 \n 7 | 8 | 9')

    while not response:
        move = input()
        if move.isdigit():
            move = int(move)
            if move < 1 or move > 9:
                print(f'\n\nImpossible move please try again.')
            elif gameBoard[move - 1] != ' ':
                print(f'\n\nThat position is already taken! Try again.')
            else:
                return move
        else: print('Invalid response')

def checkGameState(gameBoard):
    gameOver = False
    tie = False
    winCons = [[0, 1, 2], [3, 4, 5], [6, 7, 8], \
               [0, 3, 6], [1, 4, 7], [2, 5, 8], \
               [0, 4, 8], [2, 4, 6]]
    
    for win in winCons:
        check = [gameBoard[v] for v in win]
        gameOver = (check.count(check[0]) == 3) and check[0] != ' '
        if gameOver: 
            print(gameOver, tie)
            return gameOver, tie

    if (' ' not in gameBoard):
        tie = True
        gameOver = True
        return gameOver, tie
    else: return gameOver, tie
        
game()  