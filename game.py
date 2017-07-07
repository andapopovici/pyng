import pygame
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = (700, 500)

# Paddle constants
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
# the X coord of the right paddle
RIGHT_PADDLE_X = 695
PADDLE_MIN_Y = 0
PADDLE_MAX_Y = 500
# the speed with which we move the paddle
PADDLE_SPEED = 5

# Ball constants
BALL_DIMENSION = 10

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

# Starting position of the rectangle
rect_x = 50
rect_y = 50
# Speed and direction of rectangle
rect_change_x = 4
rect_change_y = 4

def drawPaddle(topX, topY, bottomX, bottomY):
    # TODO check how this works with rectangle instead
    pygame.draw.line(screen, WHITE, [topX, topY], [bottomX, bottomY], PADDLE_WIDTH)

def drawRightPaddle(topY, bottomY):
    drawPaddle(RIGHT_PADDLE_X, topY, RIGHT_PADDLE_X, bottomY)

def movePaddleBySpeed(topY_coord, bottomY_coord, speed):
    topY_coord += speed
    if topY_coord < PADDLE_MIN_Y:
        topY_coord = PADDLE_MIN_Y
        bottomY_coord = PADDLE_HEIGHT

    bottomY_coord += speed
    if bottomY_coord > PADDLE_MAX_Y:
        topY_coord = PADDLE_MAX_Y - PADDLE_HEIGHT
        bottomY_coord = PADDLE_MAX_Y

    return topY_coord, bottomY_coord

while not done:
    # --- Limit to 60 frames per second
    clock.tick(60)
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('go up')
                speed = -PADDLE_SPEED
                print(speed)
            elif event.key == pygame.K_DOWN:
                print('go down')
                speed = PADDLE_SPEED
                print(speed)
        elif event.type == pygame.KEYUP:
            speed = 0
            print('key released')
            print(speed)

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    topY_coord, bottomY_coord = movePaddleBySpeed(topY_coord, bottomY_coord, speed)
    drawRightPaddle(topY_coord, bottomY_coord)

    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, BALL_DIMENSION, BALL_DIMENSION])

    rect_x += rect_change_x
    rect_y += rect_change_y
    # Bounce the rectangle if needed
    if rect_y > 490 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 690 or rect_x < 0:
        rect_change_x = rect_change_x * -1

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
