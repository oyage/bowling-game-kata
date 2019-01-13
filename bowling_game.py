class Game(object):
    """docstring for Game."""

    def __init__(self, *args, **kwargs):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        score = 0
        roll = 0

        for frame in range(10):
            if self._is_strike(roll):
                score += 10 + self._strike_bonus(roll)
                roll += 1
            elif self._is_spare(roll):
                score += 10 + self._spare_bonus(roll)
                roll += 2
            else:
                score += self._sum_of_balls_in_frame(roll)
                roll += 2
        return score

    def _is_strike(self, roll):
        return self.rolls[roll] == 10

    def _is_spare(self, roll):
        return self.rolls[roll] + self.rolls[roll + 1] == 10
    
    def _sum_of_balls_in_frame(self, roll):
        return self.rolls[roll] + self.rolls[roll + 1]
    
    def _spare_bonus(self, roll):
        return self.rolls[roll + 2]

    def _strike_bonus(self, roll):
        return self.rolls[roll + 1] + self.rolls[roll + 2]