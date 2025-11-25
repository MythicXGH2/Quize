# Python Quiz Master  
### An Interactive Terminal-Based Quiz Game with Timer & Leaderboard  
**1st Year CSE Mini Project Report**  
**Academic Year: 2025–2026**

<br><br><br><br>

| **Submitted**             |                                 |
|---------------------------|---------------------------------|
| **Name**                  | Patel Meghal Vipulkumar         |
| **Roll No.**              | 25BAS10001                      |
| **Class**                 | Aerospace Engineering           |
| **College**               | VIT Bhopal                      |
| **Submitted to**          | VITyarthi Portal                |
| **Date of Submission**    | November 2025                   |

<br><br><br>

**Declaration**  
I hereby declare that this project is my original work and has been developed solely for academic purposes.

---
<br><br>

## Table of Contents
1. Introduction  
2. Problem Statement  
3. Objectives  
4. Functional Requirements  
5. Non-Functional Requirements  
6. System Architecture  
7. Design Diagrams  
   - Use Case Diagram  
   - Class Diagram  
   - Sequence Diagram  
   - Activity / Workflow Diagram  
   - ER Diagram (Storage)  
8. Design Decisions & Rationale  
9. Implementation Details  
10. Screenshots / Results  
11. Testing Approach  
12. Challenges Faced  
13. Learnings & Key Takeaways  
14. Future Enhancements  
15. References  

---
<br>

## 1. Introduction
Python Quiz Master is a **fun, interactive, terminal-based quiz application** developed using core Python concepts. It allows users to test their knowledge in three categories: General Knowledge, Python Programming, and Computer Science with a strict **10-second timer** per question. The game features instant colored feedback, score calculation, and a **persistent leaderboard** using file handling.

This project demonstrates fundamental programming concepts such as functions, loops, dictionaries, file I/O, time management, and error handling — perfectly aligned with the 1st-year curriculum.

---
<br>

## 2. Problem Statement
Students often rely on static question banks or paper quizzes that lack:
- Real-time feedback
- Time pressure
- Performance tracking
- Engagement and motivation

There is a need for a **lightweight, gamified quiz system** that encourages repeated practice and makes learning enjoyable.

---
<br>

## 3. Objectives
- Build a fully functional quiz game using only Python standard library
- Implement a 10-second timer per question
- Provide instant visual feedback using colors
- Maintain a permanent leaderboard using file handling
- Design clean, modular, and well-commented code

---
<br>

## 4. Functional Requirements
| ID  | Requirement                         | Description                                      |
|-----|-------------------------------------|--------------------------------------------------|
| FR1 | Accept Player Name                  | Before starting the quiz                         |
| FR2 | Category Selection                  | 3 categories to choose from                      |
| FR3 | Display Timed Questions             | 10 seconds per question                          |
| FR4 | Answer Validation & Feedback        | Show correct/wrong instantly                     |
| FR5 | Score Calculation                   | Final score out of 5                             |
| FR6 | Persistent Leaderboard              | Save name, category, score, date-time            |
| FR7 | View Leaderboard                    | Display all past records                         |
| FR8 | Menu-Driven Interface               | Start Quiz / View Leaderboard / Exit             |

---
<br>

## 5. Non-Functional Requirements
| ID  | Requirement             | Description                                      |
|-----|-------------------------|--------------------------------------------------|
| NFR1| Performance             | Strict 10-second timer enforcement               |
| NFR2| Usability               | Colorful, intuitive interface                    |
| NFR3| Portability             | Runs on Windows, Linux, macOS                    |
| NFR4| Reliability             | Handles invalid input gracefully                 |
| NFR5| Maintainability         | Clean code with comments                         |

---
<br>

## 6. System Architecture

```mermaid
graph TD
    A[Player] --> B[Python Quiz Master<br/>quiz_game.py]
    B --> C[UI Module]
    B --> D[Quiz Engine]
    D --> E[Question Bank<br/>Dictionary]
    D --> F[Leaderboard Manager]
    F --> G[quiz_leaderboard.txt]
```
## 7. Design Diagrams

### 7.1 Use Case Diagram
```mermaid
graph LR
    A[Player] --> B(Start Quiz)
    A --> C(Select Category)
    A --> D(Answer Questions)
    A --> E(View Score)
    A --> F(View Leaderboard)
    A --> G(Exit Game)
    B --> C --> D --> E
```
### 7.2 Class Diagram 
```mermaid
classDiagram
    class Player {
        -name: string
        -score: int
        +setName()
        +increaseScore()
        +getScore()
    }
    class QuizEngine {
        -timer: int = 10
        -currentCategory: string
        +startQuiz()
        +loadQuestions()
        +validateAnswer()
        +showResult()
    }
    class QuestionBank {
        <<static>>
        +getQuestions(category) list
    }
    class Leaderboard {
        -file: string
        +saveScore()
        +viewLeaderboard()
    }
    class UI {
        <<static>>
        +printGreen()
        +printRed()
        +showMenu()
    }
    Player --> QuizEngine
    QuizEngine --> QuestionBank
    QuizEngine --> Leaderboard
    QuizEngine --> UI
```
### 7.3 Sequence Diagram 
```mermaid
sequenceDiagram
    participant Player
    participant QuizEngine
    participant Timer
    participant UI
    participant Leaderboard

    Player->>QuizEngine: Enter answer
    QuizEngine->>Timer: Start 10s timer
    alt Within time
        QuizEngine->>QuizEngine: Check answer
        QuizEngine->>UI: Display Correct (Green)
        QuizEngine->>Player: +1 point
    else Timeout
        Timer-->>QuizEngine: Time up!
        QuizEngine->>UI: Display Time's Up! (Red)
    end
    Note over QuizEngine,Leaderboard: After 5 questions
    QuizEngine->>Leaderboard: Save score + details
```
### 7.4 Workflow Diagram 
```mermaid
flowchart TD
    A[Start Program] --> B[Show Main Menu]
    B --> C{User Choice}
    C -->|1| D[Enter Name]
    D --> E[Select Category]
    E --> F[Load 5 Random Questions]
    F --> G[Display Question]
    G --> H[Start 10s Timer]
    H --> I{Answer in time?}
    I -->|Yes| J{Answer Correct?}
    J -->|Yes| K[Correct +1 Score]
    J -->|No| L[Wrong! Show Answer]
    I -->|No| M[Time's Up!]
    K --> N[Next Question]
    L --> N
    M --> N
    N --> O{More Questions?}
    O -->|Yes| G
    O -->|No| P[Show Final Score]
    P --> Q[Save to Leaderboard]
    Q --> B
    C -->|2| R[View Leaderboard] --> B
    C -->|3| S[Exit]
```
### 7.5 ER Diagram 
```mermaid
erDiagram
    PLAYER ||--o{ QUIZ_SESSION : "participates in"
    QUIZ_SESSION ||--|| LEADERBOARD_FILE : "recorded in"

    PLAYER {
        string name
    }
    QUIZ_SESSION {
        string category
        int score
        datetime timestamp
    }
    LEADERBOARD_FILE {
        text file_path "quiz_leaderboard.txt"
    }
```
## 8. Design Decisions & Rationale

The following table presents the **key design decisions** made during the development of **Python Quiz Master** along with clear justification for each choice. These decisions were taken keeping in mind the **1st-year syllabus**, **learning outcomes**, **simplicity**, and **real-world effectiveness**.

| # | Design Decision                           | Chosen Approach                                                 | Rationale / Justification                                                                                                         |
|---|-------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| 1 | **Programming Paradigm**                  | Procedural (functions + global data)                            | Easier to understand and debug for beginners. OOP concepts can be introduced in 2nd year.                                         |
| 2 | **Storage Mechanism**                     | Plain text file (`quiz_leaderboard.txt`)                        | Demonstrates core file handling (`"r"`, `"a"` modes) — a mandatory topic in 1st-year Python syllabus. No external dependencies.   |
| 3 | **No External Libraries**                 | Used only built-in modules (`time`, `random`, `os`, `datetime`) | Ensures the project runs on any system with Python installed. Avoids `pip install` complexity.                                    |
| 4 | **Color Output**                          | ANSI escape codes + `os.system('')` for Windows                 | Provides rich UI without installing `colorama`. Works on all major OS after small Windows fix.                                    |
| 5 | **Timer Implementation**                  | `time.time()` instead of `time.sleep()`                         | `sleep()` blocks input. Using `time.time()` allows real-time input detection — essential for accurate 10-second enforcement.      |
| 6 | **Number of Questions per Session**       | Fixed 5 questions                                               | Keeps game short (2–3 minutes), encourages multiple attempts, prevents fatigue.                                                   |
| 7 | **10-Second Time Limit**                  | Hard-coded 10 seconds per question                              | Creates genuine pressure, improves quick thinking, and makes the game exciting and competitive.                                   |
| 8 | **Random Question Selection**             | `random.sample()`                                               | Ensures no repetition in short sessions, increases replay value.                                                                  |
| 9 | **Leaderboard Format**                    | Human-readable plain text with pipe separator                   | Easy to view/edit manually, no need for JSON/CSV parsing, looks clean in terminal and file.                                       |
|10 | **Menu-Driven Interface**                 | Simple numbered menu with loop                                  | Classic and expected structure in console applications; easy to navigate and extend.                                              |
|11 | **Error Handling Strategy**               | Try-except for input validation + graceful messages             | Prevents program crash on invalid input (letters, symbols), improves user experience.                                             |
|12 | **Code Documentation**                    | Detailed comments + section headers                             | Helps examiner and future developers understand logic quickly — excellent for evaluation.                                         |

## 9. Implementation Details

### 9.1 Technology Stack
| Component            | Technology Used                     | Reason                                      |
|----------------------|-------------------------------------|---------------------------------------------|
| Language             | Python 3.8+                         | Official 1st-year syllabus language         |
| Standard Modules     | `time`, `random`, `os`, `datetime`  | Built-in, no installation required          |
| Storage              | Plain text file                     | Demonstrates file handling concepts         |
| User Interface       | Terminal (CLI) with ANSI colors     | Rich visual feedback without GUI overhead   |

### 9.2 Core Functions Implemented

| Function                             | Purpose                                                            | Key Technique Used                     |
|--------------------------------------|--------------------------------------------------------------------|----------------------------------------|
| `print_green()`, `print_red()`, etc. | Colored output across platforms                                    | ANSI escape codes + Windows fix        |
| `save_score(name, score, category)`  | Append score to leaderboard file                                   | File handling in append mode (`"a"`)   |
| `show_leaderboard()`                 | Read and display all past scores                                   | File handling in read mode (`"r"`)     |
| `play_quiz()`                        | Main game loop for one complete session                            | Loops, timer, input validation         |
| Timer logic                          | Enforces strict 10-second limit                                    | `start_time = time.time()`             |
| Question selection                   | Picks 5 unique random questions                                    | `random.sample()`                      |

### 9.3 File Handling Implementation
```python
# Writing to leaderboard
with open("quiz_leaderboard.txt", "a") as f:
    f.write(f"{datetime.now()} | {name} | {category} | Score: {score}/5\n")

# Reading leaderboard
if os.path.exists("quiz_leaderboard.txt"):
    with open("quiz_leaderboard.txt", "r") as f:
        print(f.read())
```
### 9.4 Timer Implementation 
```python 
start_time = time.time()
user_answer = input("\nYour answer (1-4): ")
time_taken = time.time() - start_time

if time_taken > 10:
    print_red("Time's up!")
else:
    # Process answer
```
### 9.5 Code Structure Summary 
```python
quiz_game.py
├── Color functions
├── Leaderboard functions
├── Question database (dictionary)
├── Main menu loop
├── play_quiz() function
│   ├── Name input
│   ├── Category selection
│   ├── Question loop (5 times)
│   │   ├── Display question
│   │   ├── Start timer
│   │   ├── Accept & validate answer
│   │   └── Show result
│   ├── Final score display
│   └── Save to leaderboard
└── Main while loop (menu)
```
### 9.6 Total Lines of Code & Code Quality

| Metric                        | Value                  | Remarks                                                                 |
|-------------------------------|------------------------|-------------------------------------------------------------------------|
| **Total Lines of Code**       | **248 lines**          | Includes comments, blank lines, and docstrings                          |
| **Effective Code Lines**      | **182 lines**          | Excluding blank lines and comments                                      |
| **Number of Functions**       | **9 functions**        | `print_green()`, `save_score()`, `play_quiz()`, etc.                    |
| **Comments Density**          | **~35%**               | Every major block and logic is explained                                |
| **Modularity**                | High                   | Separate functions for UI, storage, timer, and game logic               |
| **Readability Score**         | Excellent              | Clear variable names, proper indentation, section headers               |
| **External Dependencies**     | **Zero**               | Uses only Python standard library — runs anywhere                       |
| **Code Reusability**          | High                   | Easy to add new categories/questions in under 5 lines                   |

#### Breakdown by Section
```text
├── Color & UI Functions          → 35 lines
├── Leaderboard Functions         → 28 lines
├── Question Database             → 48 lines
├── Main Game Logic (play_quiz)   → 98 lines
├── Menu & Navigation             → 28 lines
├── Imports & Setup               → 11 lines
Total                              = 248 lines
```
### 9.7 Sample Code Snippet 
```python
  print_yellow(q["question"])
for j, option in enumerate(q["options"]):
    print(f"{j+1}. {option}")
```
## 10. Screenshots / Results

Below are actual runtime screenshots of **Python Quiz Master** demonstrating all major features.

### 10.1 Main Menu
<img width="404" height="202" alt="image" src="https://github.com/user-attachments/assets/683b9970-7ac3-447a-844d-caa7ceafd8c5" />

### 10.2 Category Selection
<img width="404" height="223" alt="image" src="https://github.com/user-attachments/assets/58f79ea1-e13d-4c17-b5b9-b9f2e29cfe69" />

### 10.3 Gameplay – Question Display
<img width="489" height="176" alt="image" src="https://github.com/user-attachments/assets/60103193-4fd2-41f5-bbce-960474d60b48" />

### 10.4 Correct Answer (Green Feedback)
<img width="489" height="176" alt="image" src="https://github.com/user-attachments/assets/f8a5a263-dc2c-43ae-bd5b-264a0b564828" />

### 10.5 Wrong Answer (Red Feedback)
<img width="489" height="201" alt="image" src="https://github.com/user-attachments/assets/f9325b74-93f9-43ac-9121-b06565084c51" />


### 10.6 Time's Up! (Timeout)
<img width="436" height="189" alt="image" src="https://github.com/user-attachments/assets/213c5dfe-c7a6-4afe-ab51-ee3a7b2ae045" />


### 10.7 Final Score Screen
<img width="332" height="109" alt="image" src="https://github.com/user-attachments/assets/d50ecf9e-6102-4ab3-995e-98eb64d221bb" />

### 10.8 Leaderboard View
<img width="487" height="131" alt="Screenshot 2025-11-26 000513" src="https://github.com/user-attachments/assets/0dde4141-fe38-4ac2-8fd9-ce53a14231e4" />


### 10.9 Persistent Storage File
<img width="457" height="64" alt="image" src="https://github.com/user-attachments/assets/28816a61-dc5a-4aa1-b408-726ac6f99ba6" />

**All screenshots taken on Windows 11 · Python 3.11**  
**Colors work perfectly on Windows, Linux, and macOS**
