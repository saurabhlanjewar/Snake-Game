import pygame, random, math, time, sys

# intialize the pygame
pygame.init()

SCREEN_WIDTH = 800
# Create the screen
screen  = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))

# Game area dimenision 600 X 600
AREA_START_POINT = 100 #  X1 =100 , Y1 = 100
AREA_END_POINT = 700  # X2 = 700 , Y2 = 700

# Caption
pygame.display.set_caption("Snake Game")

# Game variable
FPS = 10
CLOCK = pygame.time.Clock()

# Color and font
green = (0, 255, 0)
gray = (220, 220, 220)
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255,255,255)
font = 'times new roman'

# Snake property
X1_SNAKE = 200
Y1_SNAKE = 200
WIDTH = 20
CHANGE_X = 0
CHANGE_y = 0
snake_List= []
Length_of_snake = 1

# score count
score = 0

# generate random snake food position
X1_FOOD = round(random.randrange(AREA_START_POINT, AREA_END_POINT-WIDTH) / 20) * 20
Y1_FOOD= round(random.randrange(AREA_START_POINT, AREA_END_POINT-WIDTH) / 20) * 20

# create a grid
def drawGrid():
    x = AREA_START_POINT
    y = AREA_START_POINT
    row  = (AREA_END_POINT -AREA_START_POINT) // 20 # area  600 x 600  row  = 600//20
    dim  = 600 # width of game area
    pygame.draw.line(screen,gray,(x ,AREA_START_POINT),(x,AREA_END_POINT))
    pygame.draw.line(screen,gray,(AREA_START_POINT,y),(AREA_END_POINT,y))
    pygame.draw.line(screen,gray,(x+dim,AREA_START_POINT),(x+dim,AREA_END_POINT))
    pygame.draw.line(screen,gray,(AREA_START_POINT,y+dim),(AREA_END_POINT,y+dim))

# draw the snake on the screen
def drawSnake(snake_List):
    for x in snake_List:
        pygame.draw.rect(screen, green, (x[0], x[1], WIDTH, WIDTH))

# create a score board
def showScore(choice, color, font, size):
    scoreFont = pygame.font.SysFont(font, size)
    scoreArea = scoreFont.render('Score : ' + str(score), True, color)
    scoreBox = scoreArea.get_rect()
    if choice == 1:
        scoreBox.midtop = (SCREEN_WIDTH/2, 14)
    else:
        scoreBox.midtop = (SCREEN_WIDTH/2, SCREEN_WIDTH/2)
    screen.blit(scoreArea, scoreBox)

# create game over
def gameOver():
    gameOverFont = pygame.font.SysFont(font, 90)
    gameOverArea = gameOverFont.render('YOU DIED', True, green)
    gameOverBox = gameOverArea.get_rect()
    gameOverBox.midtop = (SCREEN_WIDTH/2, SCREEN_WIDTH/4)
    screen.fill(black)
    screen.blit(gameOverArea, gameOverBox)
    showScore(0, red,font, 30)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# Game Loop
done = False
while not done:
    screen.fill((0,0,0))
    drawGrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_LEFT]:
                CHANGE_X = -20
                CHANGE_y = 0
            elif keys[pygame.K_RIGHT]:
                CHANGE_X = 20
                CHANGE_y = 0

            elif keys[pygame.K_UP]:
                CHANGE_X = 0
                CHANGE_y = -20

            elif keys[pygame.K_DOWN]:
                CHANGE_y = 20
                CHANGE_X = 0

    X1_SNAKE += CHANGE_X
    Y1_SNAKE += CHANGE_y

    # draw the snake food on the screen
    pygame.draw.rect(screen,blue,(X1_FOOD,Y1_FOOD,WIDTH,WIDTH))
    snake_Head = []
    snake_Head.append(X1_SNAKE)
    snake_Head.append(Y1_SNAKE)
    snake_List.append(snake_Head)

    if len(snake_List) > Length_of_snake:
        del snake_List[0]

    drawSnake(snake_List)

    if X1_SNAKE == X1_FOOD and Y1_SNAKE == Y1_FOOD:
        X1_FOOD = round(random.randrange(AREA_START_POINT, AREA_END_POINT-WIDTH) / 20) * 20
        Y1_FOOD= round(random.randrange(AREA_START_POINT, AREA_END_POINT-WIDTH) / 20) * 20
        Length_of_snake += 1
        score +=1

   # Touch the border game
    if X1_SNAKE < AREA_START_POINT or X1_SNAKE > AREA_END_POINT-WIDTH:
        gameOver()
    if Y1_SNAKE < AREA_START_POINT or Y1_SNAKE > AREA_END_POINT-WIDTH:
        gameOver()

    # Touch the snake body game over
    for block in snake_List[:-1]:
        if  snake_Head[0]== block[0] and snake_Head[1] == block[1]:
            gameOver()

    # show the score on the screen
    showScore(1, white, font, 30)

    pygame.display.update()

    CLOCK.tick(FPS)
