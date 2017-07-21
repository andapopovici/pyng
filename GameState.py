from GameScreen import GameScreen

class GameState:
    def __init__(self):
        self.scoreLeft = 0
        self.scoreRight = 0
        self.screen = GameScreen.START_MENU

    def incrementLeftScore(self):
        self.scoreLeft += 1

    def incrementRightScore(self):
        self.scoreRight += 1

    def startGame(self):
        self.screen = GameScreen.PLAY

    def displayScore(self):
        self.screen = GameScreen.SCORE_DISPLAY

    def resetScores(self):
        self.scoreLeft = 0
        self.scoreRight = 0
