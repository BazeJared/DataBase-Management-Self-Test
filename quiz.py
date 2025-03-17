import random

def load_questions(filename):
    questions = []
    current_question = None
    current_options = []
    current_answer = None
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check for question numbers in both formats (with and without colon)
        if line[0].isdigit() and ('.' in line or ':' in line):
            # Only add the previous question if it has both question and answer
            if current_question and current_answer and not any(q['question'] == current_question for q in questions):
                questions.append({
                    'question': current_question,
                    'options': current_options.copy(),
                    'answer': current_answer
                })
            current_question = line
            current_options = []
            current_answer = None
        elif line.lstrip().startswith('A.') or line.lstrip().startswith('B.') or line.lstrip().startswith('C.') or line.lstrip().startswith('D.') or line.lstrip().startswith('E.'):
            current_options.append(line.lstrip())  # Remove all leading whitespace
        elif line.lstrip().startswith('Answer:'):
            current_answer = line.lstrip().replace('Answer:', '').strip()
    
    # Add the last question if it has both question and answer
    if current_question and current_answer and not any(q['question'] == current_question for q in questions):
        questions.append({
            'question': current_question,
            'options': current_options.copy(),
            'answer': current_answer
        })
    
    # Sort questions by number to ensure correct order
    questions.sort(key=lambda x: int(''.join(filter(str.isdigit, x['question'].split('.')[0].split(':')[0]))))
    
    # Debug print final questions
    print("\nFinal Questions:")
    for q in questions:
        print(f"Question number: {q['question'].split('.')[0].strip().rstrip(':')}")
        print(f"Full question: {q['question']}")
        print("-" * 50)
    
    return questions

def is_multiple_choice(question):
    # Check if the question has options A, B, C, D, or E
    return len(question['options']) > 0

def take_quiz(questions):
    score = 0
    total = len(questions)
    
    print("\nWelcome to the Database Design Quiz!")
    print(f"There are {total} questions. Good luck!")
    print("\nInstructions:")
    print("1. For multiple choice questions, enter the letter (A, B, C, D, or E)")
    print("2. For fill-in-the-blank questions, enter your answer")
    print("3. For questions with multiple answers, separate them with a comma (e.g., 'A,C' or 'rectangles,diamonds')")
    print("4. Answers are not case-sensitive\n")
    
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}:")
        print(q['question'])
        
        # Check if this is a multiple choice question
        if is_multiple_choice(q):
            print("\nOptions:")
            for option in q['options']:
                print(option)
            print("\nEnter your answer (for multiple answers, separate with commas - e.g., A,C):")
        else:
            print("\nEnter your answer:")
        
        user_answer = input("> ").strip().upper()
        correct_answer = q['answer'].upper()
        
        # Handle multiple answers
        if ',' in correct_answer:
            correct_answers = [ans.strip() for ans in correct_answer.split(',')]
            user_answers = [ans.strip() for ans in user_answer.split(',')]
            if set(user_answers) == set(correct_answers):
                print("Correct! ✓")
                score += 1
            else:
                print(f"Incorrect. The correct answer was: {correct_answer}")
        else:
            if user_answer == correct_answer:
                print("Correct! ✓")
                score += 1
            else:
                print(f"Incorrect. The correct answer was: {correct_answer}")
        
        print("-" * 50)
    
    percentage = (score / total) * 100
    print(f"\nQuiz completed! Your score: {score}/{total} ({percentage:.1f}%)")
    
    if percentage >= 90:
        print("Excellent work! You're a database design expert!")
    elif percentage >= 70:
        print("Good job! You have a solid understanding of database design.")
    else:
        print("Keep studying! You might want to review the material again.")

def main():
    try:
        questions = load_questions('key.txt')
        random.shuffle(questions)
        take_quiz(questions)
    except FileNotFoundError:
        print("Error: key.txt file not found!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 