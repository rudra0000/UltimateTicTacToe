from utils import minimax
gameState=[
    ['x','o','x'],
    ['.','o','.'],
    ['x','.','.']
]
jool,parentscore,newState=minimax(gameState,False)
print(newState)
print(parentscore)
# altgameState=[
#     ['x','o','x'],
#     ['.','o','.'],
#     ['x','.','.']
# ]
# score=minimax(altgameState,True)[1]
# print(score)