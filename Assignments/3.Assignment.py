print("🎮 Welcome to the Python Quiz Game!")

questions = [
    {
        "question": "What will be the output of print(\"Hello\" + \"World\")?",
        "options": {
            "A": "Hello World",
            "B": "HelloWorld",
            "C": "Hello+World",
            "D": "Error"
        },
        "answer": "B"
    },
    {
        "question": "What is the output of print(2 * 3 + 1)?",
        "options": {
            "A": "7",
            "B": "9",
            "C": "8",
            "D": "5"
        },
        "answer": "A"
    },
    {
        "question": "Which of the following is a valid variable name in Python?",
        "options": {
            "A": "1number",
            "B": "number_1",
            "C": "number-1",
            "D": "number one"
        },
        "answer": "B"
    },
    {
        "question": "Which one is a Python loop keyword?",
        "options": {
            "A": "repeat",
            "B": "foreach",
            "C": "for",
            "D": "loop"
        },
        "answer": "C"
    },
    {
        "question": "Which function is used to get input from the user in Python?",
        "options": {
            "A": "get()",
            "B": "input()",
            "C": "read()",
            "D": "scan()"
        },
        "answer": "B"
    },
    {
        "question": "How do you start a comment in Python?",
        "options": {
            "A": "//",
            "B": "<!--",
            "C": "#",
            "D": "**"
        },
        "answer": "C"
    },
    {
        "question": "Which of the following is a correct list?",
        "options": {
            "A": "[1, 2, 3]",
            "B": "(1, 2, 3)",
            "C": "{1, 2, 3}",
            "D": "<1, 2, 3>"
        },
        "answer": "A"
    },
    {
        "question": "Which of the following is NOT a Python data type?",
        "options": {
            "A": "int",
            "B": "str",
            "C": "real",
            "D": "list"
        },
        "answer": "C"
    },
    {
        "question": "What is the output of print(len(\"Python\"))?",
        "options": {
            "A": "5",
            "B": "6",
            "C": "7",
            "D": "Error"
        },
        "answer": "B"
    },
    {
        "question": "Which of the following is a mutable data type?",
        "options": {
            "A": "tuple",
            "B": "string",
            "C": "list",
            "D": "int"
        },
        "answer": "C"
    },
    {
        "question": "What does a function return by default if there is no return statement?",
        "options": {
            "A": "0",
            "B": "1",
            "C": "None",
            "D": "Error"
        },
        "answer": "C"
    }
]

def run_quiz():
    score = 0
    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        for key, value in q["options"].items():
            print(f"{key}) {value}")
        while True:
            answer = input("Your answer (A/B/C/D): ").upper()
            if answer in q["options"]:
                break
            else:
                print("❌ Invalid input. Please enter A, B, C, or D.")
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            correct = q['answer']
            print(f"❌ Incorrect! The correct answer was: {correct}) {q['options'][correct]}")
    print(f"\n🎉 Quiz Completed! Your score: {score}/{len(questions)}")

run_quiz()


'''🎮 Welcome to the Python Quiz Game!

of print("Hello" + "World")?
A) Hello World
B) HelloWorld
C) Hello+World
D) Error
Your answer (A/B/C/D): b
✅ Correct!

Question 2: What is the output of print(2 * 3 + 1)?
A) 7
B) 9
C) 8
D) 5
Your answer (A/B/C/D): a
✅ Correct!

Question 3: Which of the following is a valid variable name in Python?
A) 1number
B) number_1
C) number-1
D) number one
Your answer (A/B/C/D): b
✅ Correct!

Question 4: Which one is a Python loop keyword?
A) repeat
B) foreach
C) for
D) loop
Your answer (A/B/C/D): c
✅ Correct!

Question 5: Which function is used to get input from the user in Python?
A) get()
B) input()
C) read()
D) scan()
Your answer (A/B/C/D): b
✅ Correct!

Question 6: How do you start a comment in Python?
A) //
B) <!--
C) #
D) **
Your answer (A/B/C/D): c
✅ Correct!

Question 7: Which of the following is a correct list?
A) [1, 2, 3]
B) (1, 2, 3)
C) {1, 2, 3}
D) <1, 2, 3>
Your answer (A/B/C/D): a
✅ Correct!

Question 8: Which of the following is NOT a Python data type?
A) int
B) str
C) real
D) list
Your answer (A/B/C/D): c
✅ Correct!

Question 9: What is the output of print(len("Python"))?
A) 5
B) 6
C) 7
D) Error
Your answer (A/B/C/D): b
✅ Correct!

Question 10: Which of the following is a mutable data type?
A) tuple
B) string
C) list
D) int
Your answer (A/B/C/D): c
✅ Correct!

Question 11: What does a function return by default if there is no return statement?
A) 0
B) 1
C) None
D) Error
Your answer (A/B/C/D): c
✅ Correct!

🎉 Quiz Completed! Your score: 11/11'''