questions = [
    "1. How many colors are there in rainbows: ? ",
    "2. President of usa: ? ",
    "3. Grams in kg: ?"
]


answers = ["7", "trump", "1000"]


score = 0

for i in range(len(questions)):
    user_answer = input(questions[i]).lower()
    if user_answer == answers[i]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answers[i].capitalize()}.")


print(f"\nYou got {score} out of {len(questions)} correct!")
