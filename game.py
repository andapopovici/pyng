import random
import pygame

from Ball import Ball
from Paddle import Paddle
import constants

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(constants.SCREEN_SIZE)
pygame.display.set_caption(constants.GAME_TITLE)

rightPaddle = Paddle(
                constants.RIGHT_PADDLE_X,
                constants.PADDLE_Y,
                constants.PADDLE_MIN_Y,
                constants.PADDLE_MAX_Y,
                constants.PADDLE_HEIGHT,
                constants.PADDLE_WIDTH,
                constants.PADDLE_SPEED)

leftPaddle = Paddle(
                constants.LEFT_PADDLE_X,
                constants.PADDLE_Y,
                constants.PADDLE_MIN_Y,
                constants.PADDLE_MAX_Y,
                constants.PADDLE_HEIGHT,
                constants.PADDLE_WIDTH,
                constants.PADDLE_SPEED)

ball = Ball(constants.BALL_DIMENSION,
            constants.BALL_X,
            random.randint(constants.BALL_INITIAL_Y_RANGE[0], constants.BALL_INITIAL_Y_RANGE[1]),
            constants.BALL_MIN_X,
            constants.BALL_MAX_X,
            constants.BALL_MIN_Y,
            constants.BALL_MAX_Y,
            constants.BALL_SPEED_X,
            constants.BALL_SPEED_Y)

print("initial ball position ", ball.x, ball.y)

def drawPaddle(topX, topY):
    pygame.draw.rect(screen, constants.WHITE, [topX, topY, constants.PADDLE_WIDTH, constants.PADDLE_HEIGHT])

def drawMiddleLine():
    pygame.draw.line(screen, constants.WHITE, [constants.SCREEN_MAX_WIDTH / 2, 0],
                     [constants.SCREEN_MAX_WIDTH / 2, constants.SCREEN_MAX_HEIGHT])

scoreRight = 0
scoreLeft = 0

myfont = pygame.font.SysFont(constants.FONT_TYPE, constants.SCORE_FONT_SIZE)

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

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
    screen.fill(constants.BLACK)

    drawPaddle(leftPaddle.x, leftPaddle.y)
    drawPaddle(rightPaddle.x, rightPaddle.y)

    rightScoreTextSurface = myfont.render(str(scoreRight), True, constants.WHITE)
    screen.blit(rightScoreTextSurface, (constants.LEFT_SCORE_X, constants.SCORE_Y))

    leftScoreTextSurface = myfont.render(str(scoreLeft), True, constants.WHITE)
    screen.blit(leftScoreTextSurface, (constants.RIGHT_SCORE_X, constants.SCORE_Y))

    drawMiddleLine()

    pygame.draw.circle(screen, constants.WHITE, (ball.x, ball.y), ball.dimension)

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
