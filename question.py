class Question:
    """
    Represents a single quiz question.
    """

    def __init__(self, question, options, answer, difficulty, explanation):

        self.question = question
        self.options = options
        self.answer = answer
        self.difficulty = difficulty
        self.explanation = explanation

    def display(self):

        print("\n" + "-" * 60)
        print(f"Difficulty : {self.difficulty}")
        print("-" * 60)

        print(self.question)
        print()

        letters = ["A", "B", "C", "D"]

        for i, option in enumerate(self.options):
            print(f"{letters[i]}. {option}")

        print()

    def check_answer(self, user_answer):

        letters = ["A", "B", "C", "D"]

        return letters[self.answer] == user_answer.upper()

    def get_correct_answer(self):

        letters = ["A", "B", "C", "D"]

        return f"{letters[self.answer]}. {self.options[self.answer]}"