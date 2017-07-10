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
PADDLE_HEIGHT = 100
# the X coord of the right paddle
RIGHT_PADDLE_X = 690
PADDLE_MIN_Y = 0
PADDLE_MAX_Y = 400
# the speed with which we move the paddle
PADDLE_SPEED = 5

# Ball constants
BALL_DIMENSION = 5

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My very basic Pong game")

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Speed in pixels per frame
speed = 0
# Current position
topY_coord = 200
bottomY_coord = 300

# Starting position of the ball
ball_x = 0
ball_y = random.randint(100, 350)

print("initial ball position ", ball_x, ball_y)
# Speed and direction of rectangle
ball_change_x = 5
ball_change_y = 5

def drawPaddle(topX, topY):
    pygame.draw.rect(screen, WHITE, [topX, topY, PADDLE_WIDTH, PADDLE_HEIGHT])

def drawRightPaddle(topY):
    drawPaddle(RIGHT_PADDLE_X, topY)

def movePaddleBySpeed(topY_coord, speed):
    topY_coord += speed

    if topY_coord < PADDLE_MIN_Y:
        topY_coord = PADDLE_MIN_Y

    if topY_coord > PADDLE_MAX_Y:
        topY_coord = PADDLE_MAX_Y

    return topY_coord

while not done:
    # --- Limit to 60 frames per second
    clock.tick(60)

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed = -PADDLE_SPEED
            elif event.key == pygame.K_DOWN:
                speed = PADDLE_SPEED
        elif event.type == pygame.KEYUP:
            speed = 0

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    topY_coord = movePaddleBySpeed(topY_coord, speed)
    drawRightPaddle(topY_coord)

    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_DIMENSION, 0)

    ball_x += ball_change_x
    ball_y += ball_change_y

    # Bounce the rectangle if needed
    if ball_y > MAX_HEIGHT - BALL_DIMENSION or ball_y < 0:
        ball_change_y = ball_change_y * -1
    if ball_x > MAX_WIDTH - PADDLE_WIDTH or ball_x < 0:
        ball_change_x = ball_change_x * -1

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
