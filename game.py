import random
import pygame

import constants
from Ball import Ball
from Paddle import Paddle
from GameState import GameState
from draw_utils import drawPaddle, drawMiddleLine, drawBall, drawScore

# Init
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(constants.SCREEN_SIZE)
pygame.display.set_caption(constants.GAME_TITLE)
font = pygame.font.SysFont(constants.FONT_TYPE, constants.SCORE_FONT_SIZE)

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

state = GameState()
print("initial ball position ", ball.x, ball.y)

scoreRight = 0
scoreLeft = 0

done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

while not done:
    clock.tick(constants.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_w]:
        leftPaddle.moveUp()
    if keys[pygame.K_s]:
        leftPaddle.moveDown()
    if keys[pygame.K_UP]:
        rightPaddle.moveUp()
    if keys[pygame.K_DOWN]:
        rightPaddle.moveDown()

    # Don't put other drawing commands above this, or they will be erased.
    screen.fill(constants.BLACK)

    drawPaddle(screen, leftPaddle)
    drawPaddle(screen, rightPaddle)
    drawMiddleLine(screen)
    drawBall(screen, ball)
    drawScore(screen, font, state.scoreLeft, constants.LEFT_SCORE_X)
    drawScore(screen, font, state.scoreRight, constants.RIGHT_SCORE_X)

    ball.move()

    if ball.hitsRightEdge():
        if ball.isWithinVerticalBounds(rightPaddle.y, rightPaddle.getBottomY()):
            state.incrementRightScore()
        else:
            print("Player 1 wins - restart")
            state.resetScores()

    if ball.hitsLeftEdge():
        if ball.isWithinVerticalBounds(leftPaddle.y, leftPaddle.getBottomY()):
            state.incrementLeftScore()
        else:
            print("Player 2 wins - restart")
            state.resetScores()

    pygame.display.flip()
