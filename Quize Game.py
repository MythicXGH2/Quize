# QUIZ GAME - Perfect 1st Year CSE Project
# Features: Multiple categories, Timer, Score saving, Colorful UI

import random
import time
import os
from datetime import datetime

# Colors for fun (works on Windows 10/11, Linux, Mac)
try:
    import colorama
    colorama.init()
except:
    os.system('')  # Enable ANSI on Windows

def print_green(text): print("\033[92m" + text + "\033[0m")
def print_red(text): print("\033[91m" + text + "\033[0m")
def print_yellow(text): print("\033[93m" + text + "\033[0m")
def print_cyan(text): print("\033[96m" + text + "\033[0m")

# Quiz questions (you can add more!)
questions = {
    "General Knowledge": [
        {"question": "What is the capital of India?", "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"], "answer": 0},
        {"question": "Who is known as Father of Computer?", "options": ["Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs"], "answer": 0},
        {"question": "How many continents are there?", "options": ["5", "6", "7", "8"], "answer": 2},
        {"question": "Which planet is known as Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "answer": 1},
        {"question": "What is the full form of CPU?", "options": ["Central Processing Unit", "Computer Processing Unit", "Central Program Unit", "Control Processing Unit"], "answer": 0}
    ],

    "Python Programming": [
        {"question": "Which of these is not a core data type in Python?", "options": ["List", "Dictionary", "Tuple", "Class"], "answer": 3},
        {"question": "What is the output of print(2 ** 3)?", "options": ["6", "8", "9", "None"], "answer": 1},
        {"question": "Which keyword is used to create a function?", "options": ["function", "def", "fun", "define"], "answer": 1},
        {"question": "How do you insert comments in Python?", "options": ["// comment", "!-- comment --", "# comment", "/* comment */"], "answer": 2},
        {"question": "What is the correct file extension for Python?", "options": [".pyth", ".pt", ".py", ".pyt"], "answer": 2}
    ],

    "Computer Science": [
        {"question": "What does HTML stand for?", "options": ["Hyper Text Markup Language", "High Text Markup Language", "Hyperlink Text Markup Language", "None"], "answer": 0},
        {"question": "Which is not an operating system?", "options": ["Windows", "Linux", "Oracle", "macOS"], "answer": 2},
        {"question": "1 byte = ?", "options": ["4 bits", "8 bits", "16 bits", "32 bits"], "answer": 1},
        {"question": "Who founded Apple Inc?", "options": ["Bill Gates", "Steve Jobs", "Mark Zuckerberg", "Elon Musk"], "answer": 1},
        {"question": "Which language is used for styling web pages?", "options": ["HTML", "JQuery", "CSS", "XML"], "answer": 2}
    ]
}

def save_score(name, score, category):
    with open("quiz_leaderboard.txt", "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} | {name} | {category} | Score: {score}/5\n")

def show_leaderboard():
    print_cyan("\n" + "="*50)
    print_cyan("         LEADERBOARD")
    print_cyan("="*50)
    if os.path.exists("quiz_leaderboard.txt"):
        with open("quiz_leaderboard.txt", "r") as f:
            print(f.read())
    else:
        print_yellow("No scores yet! Be the first!")
    print_cyan("="*50)

def play_quiz():
    print_cyan("""
    ╔══════════════════════════════════════════╗
      Welcome to the Ultimate Quiz Game! 🎯
    ╚══════════════════════════════════════════╝
    """)
    
    name = input("Enter your name: ")
    print("\nCategories:")
    categories = list(questions.keys())
    for i, cat in enumerate(categories):
        print(f"{i+1}. {cat}")
    
    while True:
        try:
            choice = int(input("\nChoose category (1-3): ")) - 1
            if 0 <= choice < len(categories):
                selected_category = categories[choice]
                break
            else:
                print_red("Invalid choice! Try again.")
        except:
            print_red("Please enter a number!")

    score = 0
    selected_questions = random.sample(questions[selected_category], 5)
    
    print_cyan(f"\nStarting {selected_category} Quiz! You have 10 seconds per question.\n")
    time.sleep(2)

    for i, q in enumerate(selected_questions):
        print(f"\nQuestion {i+1}/5")
        print_yellow(q["question"])
        
        for j, option in enumerate(q["options"]):
            print(f"{j+1}. {option}")
        
        start_time = time.time()
        user_answer = input("\nYour answer (1-4): ")
        time_taken = time.time() - start_time

        if time_taken > 10:
            print_red("Time's up! ⏰")
            print(f"Correct answer: {q['options'][q['answer']]}")
            continue
            
        try:
            if int(user_answer) - 1 == q["answer"]:
                print_green("Correct! +1 point")
                score += 1
            else:
                print_red("Wrong!")
                print_green(f"Correct answer: {q['options'][q['answer']]}")
        except:
            print_red("Invalid input!")
            print_green(f"Correct answer: {q['options'][q['answer']]}")
        
        print(f"Time taken: {time_taken:.1f}s\n")
        time.sleep(1)

    # Final result
    print_cyan("\n" + "="*40)
    print_cyan(f"Quiz Complete, {name}!")
    print_cyan(f"Your Score: {score}/5")
    
    if score == 5:
        print_green("Outstanding! You're a genius! 🏆")
    elif score >= 3:
        print_yellow("Good job! Keep learning! ⭐")
    else:
        print_red("Better luck next time! Try again! 💪")
    
    save_score(name, score, selected_category)
    print_cyan("="*40)

# Main menu
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print_cyan("""
    ╔═══════════════════════════════════╗
          PYTHON QUIZ MASTER 2025
    ╚═══════════════════════════════════╝
    """)
    print("1. Start Quiz")
    print("2. View Leaderboard")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ")
    
    if choice == "1":
        play_quiz()
        input("\nPress Enter to continue...")
    elif choice == "2":
        show_leaderboard()
        input("\nPress Enter to go back...")
    elif choice == "3":
        print_green("Thank you for playing! Goodbye! 👋")
        break
    else:
        print_red("Invalid choice!")
        time.sleep(1)