questions = [
    {
        "question": "Which language are we using?",
        "options": ["Java", "Python", "HTML"],
        "answer": "b"
    },
    {
        "question": "Which command lists Docker containers?",
        "options": ["docker ps", "docker build", "docker pull"],
        "answer": "a"
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["func", "define", "def"],
        "answer": "c"
    }
]

score = 0

print("=== Python Quiz ===")

for number, question in enumerate(questions, start=1):
    print(f"\n{number}. {question['question']}")

    for letter, option in zip(["a", "b", "c"], question["options"]):
        print(f"   {letter}) {option}")

    while True:
        answer = input("Your answer (a/b/c): ").strip().lower()

        if answer in ["a", "b", "c"]:
            break

        print("Invalid input. Please enter a, b, or c.")

    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

print(f"\nQuiz finished! Your score: {score}/{len(questions)}")