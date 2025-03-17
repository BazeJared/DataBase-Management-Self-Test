# DataBase-Management-Self-Test
Database Design Quiz
Overview
This is a command-line quiz application designed to test users on database design concepts. The quiz reads questions from a text file (key.txt), formats them properly, and presents them to the user in a multiple-choice or fill-in-the-blank format. The questions are randomized, and the user's score is displayed at the end of the quiz.

Features
Loads quiz questions dynamically from a file (key.txt).
Supports both multiple-choice and fill-in-the-blank questions.
Randomizes the question order for a varied experience.
Provides immediate feedback on answers.
Displays a final score and performance evaluation.
How It Works
1. Loading Questions
The load_questions(filename) function reads questions from a text file, processes them into structured data, and ensures proper formatting:

Detects question numbers and formats them correctly.
Identifies multiple-choice options (A, B, C, D, E).
Extracts correct answers from "Answer: ..." lines.
Sorts questions numerically to maintain order.
2. Taking the Quiz
The take_quiz(questions) function presents questions to the user one at a time:

Displays the question and answer choices (if applicable).
Accepts answers and compares them against the correct ones.
Supports multiple-answer inputs (e.g., "A,C" or "rectangles,diamonds").
Tracks the user’s score and displays a final percentage with feedback.
3. Running the Quiz
The main() function loads the questions, shuffles them, and starts the quiz. If the key.txt file is missing, it will display an error message.

Installation & Usage
Prerequisites
Python 3.x installed on your system.
A properly formatted key.txt file containing quiz questions.
Running the Quiz
Clone or download the script.

Ensure you have a key.txt file with questions formatted as follows:

pgsql
Copy
Edit
1. What is the primary key in a database?  
A. A unique identifier for a record  
B. A foreign key reference  
C. A randomly generated value  
D. A non-unique attribute  
Answer: A  

2. Which SQL command is used to retrieve data?  
A. SELECT  
B. UPDATE  
C. DELETE  
D. INSERT  
Answer: A  
Run the script using:

bash
Copy
Edit
python quiz.py
Follow the on-screen instructions to complete the quiz.

Error Handling
If key.txt is missing, the program will notify the user.
If an invalid input is detected, the quiz will still process the answer but may mark it incorrect.
Customization
To add more questions, simply edit key.txt following the existing format.
To modify question randomization, adjust the random.shuffle(questions) call in main().
You can change the performance feedback thresholds in the final score calculation.
License
This project is open-source. Feel free to modify and distribute it as needed.

This README should provide clear guidance for using your quiz script! Let me know if you need any modifications. 🚀