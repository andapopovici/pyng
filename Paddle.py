class Paddle:
    def __init__(self, x, y, minY, maxY, height, width):
        self.x = x
        self.y = y
        self.minY = minY
        self.maxY = maxY
        self.height = height
        self.width = width

    def move(self, step):
        self.y += step

        if self.y < self.minY:
            self.y = self.minY

        if self.y > self.maxY:
            self.y = self.maxY
