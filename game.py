import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# screen dimensions
MAX_WIDTH = 700
MAX_HEIGHT = 500

size = (MAX_WIDTH, MAX_HEIGHT)

# Paddle constants
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 90
# the X coord of the right paddle
RIGHT_PADDLE_X = MAX_WIDTH - PADDLE_WIDTH
PADDLE_MIN_Y = 0
PADDLE_MAX_Y = MAX_HEIGHT - PADDLE_HEIGHT
# the speed with which we move the paddle
PADDLE_SPEED = 5

# Ball constants
BALL_DIMENSION = 5

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My very basic Pong game")

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Speed in pixels per frame
speedRightPaddle = 0
speedLeftPaddle = 0
# Current position
rightPaddle_y = 200
leftPaddle_y = 200
# Starting position of the ball
ball_x = 10
ball_y = random.randint(100, 350)

print("initial ball position ", ball_x, ball_y)
# Speed and direction of rectangle
ball_change_x = 5
ball_change_y = 5

def drawPaddle(topX, topY):
    pygame.draw.rect(screen, WHITE, [topX, topY, PADDLE_WIDTH, PADDLE_HEIGHT])

def drawRightPaddle(topY):
    drawPaddle(RIGHT_PADDLE_X, topY)

def drawLeftPaddle(y):
    drawPaddle(0, y)

def movePaddleBySpeed(yCoord, speed):
    yCoord += speed

    if yCoord < PADDLE_MIN_Y:
        yCoord = PADDLE_MIN_Y

    if yCoord > PADDLE_MAX_Y:
        yCoord = PADDLE_MAX_Y

    return yCoord

def drawMiddleLine():
    pygame.draw.line(screen, WHITE, [MAX_WIDTH / 2, 0], [MAX_WIDTH / 2, MAX_HEIGHT], 1)

scoreRight = 0
scoreLeft = 0

myfont = pygame.font.SysFont('monospace', 30)

while not done:
    # --- Limit to 60 frames per second
    clock.tick(60)

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speedRightPaddle = -PADDLE_SPEED
            elif event.key == pygame.K_DOWN:
                speedRightPaddle = PADDLE_SPEED
            elif event.key == pygame.K_w:
                speedLeftPaddle = -PADDLE_SPEED
            elif event.key == pygame.K_s:
                speedLeftPaddle = PADDLE_SPEED
        elif event.type == pygame.KEYUP:
            speedRightPaddle = 0
            speedLeftPaddle = 0

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    rightScoreTextSurface = myfont.render(str(scoreRight), True, WHITE)
    screen.blit(rightScoreTextSurface, (370, 10))

    leftScoreTextSurface = myfont.render(str(scoreLeft), True, WHITE)
    screen.blit(leftScoreTextSurface, (310, 10))

    drawMiddleLine()

    rightPaddle_y = movePaddleBySpeed(rightPaddle_y, speedRightPaddle)
    drawRightPaddle(rightPaddle_y)
    leftPaddle_y = movePaddleBySpeed(leftPaddle_y, speedLeftPaddle)
    drawLeftPaddle(leftPaddle_y)

    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_DIMENSION, 0)

    ball_x += ball_change_x
    ball_y += ball_change_y

    # Bounce the rectangle if needed
    if ball_y > MAX_HEIGHT - BALL_DIMENSION or ball_y < 0:
        ball_change_y *= -1
    if ball_x > MAX_WIDTH - PADDLE_WIDTH or ball_x < 10:
        ball_change_x *= -1
        if ball_x > MAX_WIDTH - PADDLE_WIDTH:
            print("hit right edge", ball_y)
            if ball_y >= rightPaddle_y and ball_y <= rightPaddle_y + PADDLE_HEIGHT:
                scoreRight += 1
            else:
                scoreRight = 0
        else:
            print("hit right edge", ball_y)
            if ball_y >= leftPaddle_y and ball_y <= leftPaddle_y + PADDLE_HEIGHT:
                scoreLeft += 1
            else:
                scoreLeft = 0

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
