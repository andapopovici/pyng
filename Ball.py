class Ball:
    def __init__(self, dimension, x, y, minX, maxX, minY, maxY, changeX, changeY):
        self.dimension = dimension
        self.x = x
        self.y = y
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY
        self.changeX = changeX
        self.changeY = changeY

    def move(self):
        self.x += self.changeX
        self.y += self.changeY

        # Bounce the ball if needed
        if self.hitsBottomEdge() or self.hitsTopEdge() or self.hitsRightEdge() or self.hitsLeftEdge():
            self.changeY *= -1

    def hitsRightEdge(self):
        return True if self.x > self.maxX else False

    def hitsLeftEdge(self):
        return True if self.x < self.minX else False

    def hitsTopEdge(self):
        return True if self.y < self.minY else False

    def hitsBottomEdge(self):
        return True if self.y > self.maxY else False

    def isWithinVerticalBounds(self, min, max):
        return True if self.y >= min <= max else False
