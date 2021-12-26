class Player:

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Invalid input!")
            self._lives = 0

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("ERROR")

    @property
    def score(self):
        return self.score()

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return f"Name: {self.name}, Lives:{self.lives}, Score:{self._score}, Level:{self.level}"

