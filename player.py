class Player:
    """
    Stores all player related information.
    """

    def __init__(self, name):

        self.name = name
        self.score = 0
        self.correct = 0
        self.wrong = 0
        self.current_streak = 0
        self.best_streak = 0

    def correct_answer(self):

        self.score += 1
        self.correct += 1
        self.current_streak += 1

        if self.current_streak > self.best_streak:
            self.best_streak = self.current_streak

    def wrong_answer(self):

        self.wrong += 1
        self.current_streak = 0

    def accuracy(self):

        total = self.correct + self.wrong

        if total == 0:
            return 0

        return round((self.correct / total) * 100, 2)

    def show_statistics(self):

        print("\n" + "=" * 40)
        print("PLAYER STATISTICS")
        print("=" * 40)

        print(f"Player Name   : {self.name}")
        print(f"Correct       : {self.correct}")
        print(f"Wrong         : {self.wrong}")
        print(f"Score         : {self.score}")
        print(f"Accuracy      : {self.accuracy()}%")
        print(f"Best Streak   : {self.best_streak}")

        print("=" * 40)