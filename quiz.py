import random

from player import Player
from colors import Colors, difficulty_color

from utils import (
    banner,
    clear_screen,
    choose_topic,
    load_questions,
    get_answer,
    pause,
    progress_bar,
    save_score,
    show_high_scores
)


class Quiz:

    def __init__(self):

        self.player = None

        self.topics = load_questions()

        self.review = []

        self.total_questions = 7


    # -----------------------------
    # Start Quiz
    # -----------------------------

    def start(self):

        clear_screen()

        banner()

        print("Welcome to Python Quiz Game\n")

        name = input("Enter Your Name : ")

        if name.strip() == "":
            name = "Guest"

        self.player = Player(name)

        topic_name, questions = choose_topic(self.topics)

        random.shuffle(questions)

        questions = questions[:min(self.total_questions, len(questions))]

        self.ask_questions(topic_name, questions)


    # -----------------------------
    # Ask Questions
    # -----------------------------

    def ask_questions(self, topic_name, questions):

        total = len(questions)

        for index, question in enumerate(questions):

            clear_screen()

            banner()

            print(f"Player : {self.player.name}")

            print(f"Topic  : {topic_name}")

            print()

            print(progress_bar(index + 1, total))

            print()

            print(
                difficulty_color(question.difficulty)
                + question.difficulty
                + Colors.RESET
            )

            question.display()

            answer = get_answer()

            correct = question.check_answer(answer)

            if correct:

                print()

                print(
                    Colors.GREEN
                    + "Correct Answer!"
                    + Colors.RESET
                )

                self.player.correct_answer()

            else:

                print()

                print(
                    Colors.RED
                    + "Wrong Answer!"
                    + Colors.RESET
                )

                print()

                print(
                    "Correct Answer :",
                    question.get_correct_answer()
                )

                self.player.wrong_answer()

            print()

            print(
                Colors.YELLOW
                + "Explanation:"
                + Colors.RESET
            )

            print(question.explanation)

            self.review.append({

                "question": question.question,

                "your_answer": answer,

                "correct_answer": question.get_correct_answer(),

                "correct": correct

            })

            pause()

        self.show_result()

            # -----------------------------
    # Show Result
    # -----------------------------

    def show_result(self):

        clear_screen()

        banner()

        print("=" * 50)
        print("             QUIZ COMPLETED")
        print("=" * 50)

        self.player.show_statistics()

        save_score(self.player)

        print("\nScore has been saved successfully.")

        print("\nDo you want to review your answers?")

        choice = input("Enter (Y/N): ").strip().upper()

        if choice == "Y":
            self.show_review()

        print("\nTop High Scores")
        print("-" * 40)

        show_high_scores()

        self.play_again()


    # -----------------------------
    # Answer Review
    # -----------------------------

    def show_review(self):

        clear_screen()

        banner()

        print("=" * 60)
        print("ANSWER REVIEW")
        print("=" * 60)

        for index, item in enumerate(self.review):

            print(f"\nQuestion {index + 1}")

            print("-" * 60)

            print(item["question"])

            print()

            if item["correct"]:

                print(
                    Colors.GREEN
                    + "Your Answer : "
                    + item["your_answer"]
                    + " (Correct)"
                    + Colors.RESET
                )

            else:

                print(
                    Colors.RED
                    + "Your Answer : "
                    + item["your_answer"]
                    + Colors.RESET
                )

                print(
                    Colors.GREEN
                    + "Correct Answer : "
                    + item["correct_answer"]
                    + Colors.RESET
                )

        pause()


    # -----------------------------
    # Play Again
    # -----------------------------

    def play_again(self):

        print()

        choice = input("Play Again? (Y/N): ").strip().upper()

        if choice == "Y":

            self.review = []

            self.start()

        else:

            clear_screen()

            banner()

            print()

            print(
                Colors.CYAN
                + "Thank You For Playing!"
                + Colors.RESET
            )

            print()

            exit()