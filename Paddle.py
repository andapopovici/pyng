class Paddle:
    def __init__(self, x, y, minY, maxY, height, width, speed):
        self.x = x
        self.y = y
        self.minY = minY
        self.maxY = maxY
        self.height = height
        self.width = width
        self.speed = speed

    def getBottomY(self):
        return self.y + self.height

    def moveDown(self):
        self.y += self.speed
        self.keepWithinBounds()

    def moveUp(self):
        self.y -= self.speed
        self.keepWithinBounds()

    def keepWithinBounds(self):
        if self.y < self.minY:
            self.y = self.minY

        if self.y > self.maxY:
            self.y = self.maxY
