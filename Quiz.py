# from multiprocessing.connection import answer_challenge

questions = (("Which ear did Vincent Van Gogh cut off?"),
            ("What is the only mammal that can fly?"),
            ("What is the most frequently occurring blood type?"),
            ("What was the first toy advertised on TV?"),
            ("What is the most malleable metal?"))

options = [("A.left ", "B.right ", "C.middle ", "D.inside "),
           ("A.bat ", "B.elephant ", "C.crocodie ", "D.dog "),
           ("A.B ", "B.O ", "C.O+", "D.AB "),
           ("A.gumball ", "B.dragon ball ", "C.toy story ", "D.XXX"),
           ("A.sodium ", "B.metal ", "C.gold ", "D.sliver ")]

guesses = []
answer = ("A","A","C","D","C")
score = 0
stt = 0


for question in questions:
    print("---------------------")
    print(question)
    for option in options[stt]:
        print(option)

    guess = input("Guess your answer: ").upper()
    guesses.append(guess)

    if guess == answer[stt]:
        score += 1
        print("You are correct 😁")
    else:
        print("You are incorrect.")
        print("The correct answer was:", answer[stt])
    stt += 1

print("Your answers are: ")
for answers in answer:
    print(answers,end=",")
print(f"\nYour score was: {score}")











