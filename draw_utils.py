import pygame
import constants

def drawPaddle(screen, paddle):
    pygame.draw.rect(screen, constants.WHITE, [paddle.x, paddle.y, constants.PADDLE_WIDTH, constants.PADDLE_HEIGHT])

def drawMiddleLine(screen):
    pygame.draw.line(screen, constants.WHITE, [constants.SCREEN_MAX_WIDTH / 2, 0],
                     [constants.SCREEN_MAX_WIDTH / 2, constants.SCREEN_MAX_HEIGHT])

def drawBall(screen, ball):
    pygame.draw.circle(screen, constants.WHITE, (ball.x, ball.y), ball.dimension)

def drawScore(screen, font, score, x):
    textSurface = font.render(str(score), True, constants.WHITE)
    screen.blit(textSurface, (x, constants.SCORE_Y))
