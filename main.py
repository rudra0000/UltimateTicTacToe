from utils import minimax
import pygame,sys
pygame.init()
GREEN_COLOR=(0,255,0)
CYAN_COLOR=(0,255,255)
LINE_COLOR=GREEN_COLOR
WIDTH,HEIGHT=800,600
SQ_WIDTH,SQ_HEIGHT=100,100
SCREEN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Unbeatable Tic Tac Toe')
def draw(gameState):
    #draw vertical lines
    pygame.draw.line(SCREEN,LINE_COLOR,(WIDTH/3,0),(WIDTH/3,HEIGHT),7)
    pygame.draw.line(SCREEN,LINE_COLOR,(WIDTH/3*2,0),(WIDTH/3*2,HEIGHT),7)
    #draw horizontal lines
    pygame.draw.line(SCREEN,LINE_COLOR,(0,HEIGHT/3),(WIDTH,HEIGHT/3),7)
    pygame.draw.line(SCREEN,LINE_COLOR,(0,HEIGHT/3*2),(WIDTH,HEIGHT/3*2),7)


    for i in range(3):
        for j in range(3):
            x_dist=(WIDTH/6)*(2*(i+1)-1)-SQ_WIDTH/2
            y_dist=(HEIGHT/6)*(2*(j+1)-1)-SQ_HEIGHT/2
            if gameState[i][j]=='x':
                pygame.draw.rect(SCREEN,CYAN_COLOR,pygame.Rect(x_dist,y_dist,SQ_WIDTH,SQ_HEIGHT))
            elif gameState[i][j]=='o':
                pygame.draw.circle()

    # pygame.draw.rect(SCREEN,CYAN_COLOR,pygame.Rect(5*WIDTH/6-SQ_WIDTH/2,3*HEIGHT/6-SQ_HEIGHT/2,SQ_WIDTH,SQ_HEIGHT))
       
    #update display
    pygame.display.update()


def main():
    gameState=[
        ['o','x','o'],
        ['x','o','o'],
        ['o','.','.']
    ]
    run=True
    while run:
        #handle events
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    run=False
            elif event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        #update game state



        #draw game state
        draw(gameState)


    print(minimax(gameState,False))
    # print(findAllPossibleMoves(gameState,'o'))


if __name__=='__main__':
    main()