from utils import minimax
import pygame,sys
pygame.init()
#clock
clock=pygame.time.Clock()
FPS=60
GREEN_COLOR=(0,255,0)
CYAN_COLOR=(0,255,255)
RED_COLOR=(255,0,0)
BLUE_COLOR=(0,0,255)
LINE_COLOR=GREEN_COLOR
WIDTH,HEIGHT=800,600
SQ_WIDTH,SQ_HEIGHT=100,100
RADIUS=50
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
                pygame.draw.rect(SCREEN,RED_COLOR,pygame.Rect(x_dist,y_dist,SQ_WIDTH,SQ_HEIGHT))
            elif gameState[i][j]=='o':
                pygame.draw.circle(SCREEN,BLUE_COLOR,(x_dist+SQ_WIDTH/2,y_dist+SQ_HEIGHT/2),RADIUS)

    # pygame.draw.rect(SCREEN,CYAN_COLOR,pygame.Rect(5*WIDTH/6-SQ_WIDTH/2,3*HEIGHT/6-SQ_HEIGHT/2,SQ_WIDTH,SQ_HEIGHT))
       
    #update display
    pygame.display.update()


def main():
    gameState=[
        ['.','.','.'],
        ['.','.','.'],
        ['.','.','.']
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
            elif event.type==pygame.MOUSEBUTTONDOWN:
                x_cor,y_cor=pygame.mouse.get_pos()
                ind1=x_cor//(WIDTH/3)
                ind2=y_cor//(HEIGHT/3)
                gameState[int(ind1)][int(ind2)]='x'
                print(ind1,ind2)
                gameState=minimax(gameState,False)[2]
                if not gameState:
                    pygame.quit()
                    sys.exit()
        #update game state


        #draw game state
        draw(gameState)
        clock.tick(FPS)


if __name__=='__main__':
    main()