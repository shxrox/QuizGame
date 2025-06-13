questions = (
    "What is the capital of France?", 
    "Which language is primarily used for AI and machine learning?", 
    "What does CPU stand for?", 
    "Which planet is known as the Red Planet?", 
    "What is 5 multiplied by 6?"
)


options = (
    ("A. Paris", "B. London", "C. Rome", "D. Berlin"),  
    ("A. Java", "B. Python", "C. C++", "D. Ruby"),     
    ("A. Central Processing Unit", "B. Computer Personal Unit", "C. Central Performance Utility", "D. Control Processing Unit"),  # for Q3
    ("A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"), 
    ("A. 11", "B. 30", "C. 56", "D. 60")              
)

answers = (
    "A",  
    "B", 
    "A",  
    "B",  
    "B"   
)

guesses = []
score = 0
question_num = 0

for question in questions:
        print("---------------------")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT")
            print(f"{answers[question_num]} is the correct answer.")

        question_num += 1

print("---------------------")
print("       RESULTS       ")
print("---------------------")

print("answers : ", end=" ")
for answer in answers:
    print(answer,end=" ")
print()

print("guesses : ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your Score is : {score}%")

