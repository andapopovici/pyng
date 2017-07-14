import pygame
import random

from Ball import Ball
from Paddle import Paddle
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

rightPaddle = Paddle(
                MAX_WIDTH - PADDLE_WIDTH,
                200,
                PADDLE_MIN_Y,
                MAX_HEIGHT - PADDLE_HEIGHT,
                PADDLE_HEIGHT,
                PADDLE_WIDTH,
                PADDLE_SPEED)

leftPaddle = Paddle(
                0,
                200,
                PADDLE_MIN_Y,
                MAX_HEIGHT - PADDLE_HEIGHT,
                PADDLE_HEIGHT,
                PADDLE_WIDTH,
                PADDLE_SPEED)

ball = Ball(BALL_DIMENSION,
            10,
            random.randint(100, 350),
            10,
            MAX_WIDTH - PADDLE_WIDTH,
            0,
            MAX_HEIGHT - BALL_DIMENSION,
            5,
            5)

print("initial ball position ", ball.x, ball.y)

def drawPaddle(topX, topY):
    pygame.draw.rect(screen, WHITE, [topX, topY, PADDLE_WIDTH, PADDLE_HEIGHT])

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

    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_w]:
        leftPaddle.moveUp()
    if keys[pygame.K_s]:
        leftPaddle.moveDown()
    if keys[pygame.K_UP]:
        rightPaddle.moveUp()
    if keys[pygame.K_DOWN]:
        rightPaddle.moveDown()

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    drawPaddle(leftPaddle.x, leftPaddle.y)
    drawPaddle(rightPaddle.x, rightPaddle.y)

    rightScoreTextSurface = myfont.render(str(scoreRight), True, WHITE)
    screen.blit(rightScoreTextSurface, (370, 10))

    leftScoreTextSurface = myfont.render(str(scoreLeft), True, WHITE)
    screen.blit(leftScoreTextSurface, (300, 10))

    drawMiddleLine()

    pygame.draw.circle(screen, WHITE, (ball.x, ball.y), ball.dimension, 0)

    ball.move()

    if ball.hitsRightEdge():
        if ball.isWithinVerticalBounds(rightPaddle.y, rightPaddle.getBottomY()):
            scoreRight += 1
        else:
            # winner - Left player
            print("Player 1 wins - restart")
            scoreLeft = 0
            scoreRight = 0

    if ball.hitsLeftEdge():
        if ball.isWithinVerticalBounds(leftPaddle.y, leftPaddle.getBottomY()):
            scoreLeft += 1
        else:
            print("Player 2 wins - restart")
            scoreLeft = 0
            scoreRight = 0

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
