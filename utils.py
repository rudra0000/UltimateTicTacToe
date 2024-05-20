#check if current state is terminal and calculate the score
#game state is represented as a list of lists
def checkTerminalState(gameState):
    empty_cnt=0
    #check rows
    for row in gameState:
        empty_cnt+=row.count('.')
        if row.count(row[0])==len(row):
            if row[0]=='x':
                return True,1
            elif row[0]=='o':
                return True,-1
    #check columns
    for col in range(3):
        if gameState[col][0]==gameState[col][1] and gameState[col][1]==gameState[col][2]:
            if gameState[col][0]=='x':
                return True,1
            elif gameState[col][1]=='o':
                return True,-1
    #check diagonals
    if gameState[0][0]==gameState[1][1] and gameState[1][1]==gameState[2][2]:
        if gameState[0][0]=='x':
            return True,1
        elif gameState[0][0]=='o':
            return True,-1
    elif gameState[0][2]==gameState[1][1] and gameState[1][1]==gameState[2][0]:
        if gameState[1][1]=='x':
            return True,1
        elif gameState[1][1]=='o':
            return True,-1
    
    #check if its a draw
    if empty_cnt==0:
        return True,0
    else:
        return False,2**32-1

#minimize the score  
def checkAllPossibleMoves(gameState):
    score=2**32-1
    bestGameState=None
    for row in range(3):
        for col in range(3):
            if gameState[row][col]=='.':
                newGameState=gameState
                newGameState[row][col]='o'
                res=checkTerminalState(newGameState)
                #check if the game ends
                if res[0]:
                    if res[1]>score:
                        score=res[1]
                        bestGameState=newGameState
                #the game has not ended explore more states
                else:
                    pass
    return bestGameState

    