from utils import minimax,findAllPossibleMoves
def main():
    gameState=[
        ['o','o','x'],
        ['x','x','o'],
        ['o','.','.']
    ]
    print(minimax(gameState,False))
    # print(findAllPossibleMoves(gameState,'o'))


if __name__=='__main__':
    main()