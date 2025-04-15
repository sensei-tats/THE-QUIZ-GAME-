import json
import time
import os

# 📦 Load questions from JSON file
def load_questions(filepath="questions.json"):
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("❌ Questions file not found.")
        return []

# 📋 Ask a question and get user's answer
def ask_question(question_data):
    print("\n" + question_data["question"])
    for i, option in enumerate(question_data["options"], start=1):
        print(f"{i}. {option}")

    start_time = time.time()  # Start timer

    while True:
        try:
            user_answer = int(input("Your answer (1-4): "))
            if user_answer < 1 or user_answer > 4:
                print("Please choose a number between 1 and 4.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    end_time = time.time()
    elapsed = round(end_time - start_time, 2)
    print(f"⏱️ Time taken: {elapsed} seconds")

    if user_answer == question_data["answer"]:
        return True
    else:
        return False

# 🎮 Play the quiz
def play_quiz():
    questions = load_questions()
    if not questions:
        return

    name = input("Enter your name: ")
    score = 0

    for question in questions:
        if ask_question(question):
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {question['answer']}\n")

    print(f"🏁 Quiz Over, {name}! Your final score is {score}/{len(questions)}.")
    save_score(name, score)

# 💾 Save score to leaderboard
def save_score(name, score, filepath="leaderboard.csv"):
    with open(filepath, "a") as file:
        file.write(f"{name},{score}\n")
    print("🏆 Score saved to leaderboard.")

# 📊 Show leaderboard
def show_leaderboard(filepath="leaderboard.csv"):
    if not os.path.exists(filepath):
        print("❌ No leaderboard data found.")
        return

    print("\n📈 LEADERBOARD")
    print("-" * 30)
    with open(filepath, "r") as file:
        scores = [line.strip().split(",") for line in file]
        scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)

    for i, (name, score) in enumerate(scores[:10], start=1):
        print(f"{i}. {name} - {score} points")
    print("-" * 30)

# 🚀 Main menu
def main():
    print("🎉 Welcome to Tats DEV QUIZ")
    while True:
        print("\n1. Play Quiz")
        print("2. View Leaderboard")
        print("3. Exit")
        choice = input("Select an option (1-3): ")

        if choice == "1":
            play_quiz()
        elif choice == "2":
            show_leaderboard()
        elif choice == "3":
            print("👋 Thanks for playing!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
