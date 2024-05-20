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
        if gameState[0][col]==gameState[1][col] and gameState[1][col]==gameState[2][col]:
            if gameState[0][col]=='x':
                return True,1
            elif gameState[1][col]=='o':
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

#function to find all possible moves
def findAllPossibleMoves(gameState,player):
    allPossibleGameStates=[]
    for row in range(3):
        for col in range(3):
            if gameState[row][col]=='.':
                newGameState=[ele[:] for ele in gameState]
                newGameState[row][col]=player
                allPossibleGameStates.append(newGameState)
                # print(f'old game state is {gameState}')
    return allPossibleGameStates 

#human->maximizer
#computer->minimizer
#function will return best possible value of a state for each player
#isTerminalState,score,best move if not a terminal state
def minimax(gameState,isHumanTurn):
    res=checkTerminalState(gameState)
    if res[0]:
        return True,res[1],None
    else:
        bestPossibleGameState=None
        allStates=None
        if isHumanTurn: #maximize
            allStates=findAllPossibleMoves(gameState,'x')
            score=-2**32-1
            for state in allStates:
                value=minimax(state,False)
                if value[1]>score:
                    score=value[1]
                    bestPossibleGameState=state
        else: #minimize
            allStates=findAllPossibleMoves(gameState,'o')
            score=2**32-1
            for state in allStates:
                value=minimax(state,True)
                if value[1]<score:
                    score=value[1]
                    bestPossibleGameState=state
        return False,score,bestPossibleGameState
