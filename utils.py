import os
import json
import random

from colors import Colors
from question import Question

# -----------------------------
# Absolute Paths
# -----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

QUESTION_FILE = os.path.join(BASE_DIR, "data", "questions.json")
SCORE_FILE = os.path.join(BASE_DIR, "data", "scores.json")


# -----------------------------
# Clear Screen
# -----------------------------

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# -----------------------------
# Banner
# -----------------------------

def banner():

    print(Colors.CYAN + Colors.BOLD)

    print("╔══════════════════════════════════════════╗")
    print("║            PYTHON QUIZ GAME             ║")
    print("╚══════════════════════════════════════════╝")

    print(Colors.RESET)


# -----------------------------
# Progress Bar
# -----------------------------

def progress_bar(current, total):

    width = 30

    filled = int((current / total) * width)

    bar = "█" * filled + "░" * (width - filled)

    return f"[{bar}] {current}/{total}"


# -----------------------------
# Load Questions
# -----------------------------

def load_questions():

    try:

        with open(QUESTION_FILE, "r", encoding="utf-8") as file:

            data = json.load(file)

    except FileNotFoundError:

        print("questions.json not found!")
        return {}

    except json.JSONDecodeError:

        print("questions.json contains invalid JSON!")
        return {}

    topics = {}

    for topic, values in data.items():

        questions = []

        for item in values:

            q = Question(

                item["question"],
                item["options"],
                item["answer"],
                item["difficulty"],
                item["explanation"]

            )

            questions.append(q)

        topics[topic] = questions

    return topics


# -----------------------------
# Random Questions
# -----------------------------

def random_questions(topics):

    all_questions = []

    for questions in topics.values():

        all_questions.extend(questions)

    random.shuffle(all_questions)

    return all_questions


# -----------------------------
# Save Score
# -----------------------------

def save_score(player):

    try:

        with open(SCORE_FILE, "r", encoding="utf-8") as file:

            scores = json.load(file)

    except:

        scores = []

    scores.append({

        "name": player.name,

        "score": player.score,

        "accuracy": player.accuracy()

    })

    with open(SCORE_FILE, "w", encoding="utf-8") as file:

        json.dump(scores, file, indent=4)


# -----------------------------
# High Scores
# -----------------------------

def show_high_scores():

    try:

        with open(SCORE_FILE, "r", encoding="utf-8") as file:

            scores = json.load(file)

    except:

        print("No High Scores Yet.")
        return

    if not scores:

        print("No High Scores Yet.")
        return

    scores.sort(key=lambda x: x["score"], reverse=True)

    print("\nHIGH SCORES\n")

    for i, score in enumerate(scores[:10]):

        print(
            f"{i+1}. {score['name']} | Score : {score['score']} | Accuracy : {score['accuracy']}%"
        )


# -----------------------------
# Choose Topic
# -----------------------------

def choose_topic(topics):

    clear_screen()

    banner()

    topic_names = list(topics.keys())

    print("Choose Topic\n")

    for i, topic in enumerate(topic_names):

        print(f"{i+1}. {topic}")

    print(f"{len(topic_names)+1}. Random")

    while True:

        choice = input("\nEnter Choice : ")

        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= len(topic_names):

                selected = topic_names[choice - 1]

                return selected, topics[selected]

            elif choice == len(topic_names) + 1:

                return "Random", random_questions(topics)

        print("Invalid Choice. Try Again.")


# -----------------------------
# Pause
# -----------------------------

def pause():

    input("\nPress ENTER to Continue...")


# -----------------------------
# Answer Input
# -----------------------------

def get_answer():

    while True:

        answer = input("\nYour Answer (A/B/C/D): ").strip().upper()

        if answer in ["A", "B", "C", "D"]:

            return answer

        print("Invalid Input.")