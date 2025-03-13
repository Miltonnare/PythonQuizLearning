def quiz():
    Lists=[ "Which of the following is a Python data type?",
        "Who directed the movie 'Inception'?", 
        "What is the capital of France?",
        "Who facilitated the Killing of Gadaffi?"
        ]
    Answers = ["float", "Christopher Nolan", "Paris", "NATO"]
    score=0
    for x  in range (len(Lists)):
        print(Lists[x])
        inputter=input("You Anwser: ")

        if inputter.lower()==Answers[x].lower():
            print("Correct\n")
            score+=1

    
        else:
            print("Wrong!\n")

    print(f"Hurray! Quiz Over!Your score is {score}/{len(Lists)}")
while True:
    quiz()

    print("Do you want to Proceed? YES or NO")
    inpuu=input("Enter your Choice: ")
    if inpuu.strip().lower()!="yes":
        print("Bye! Till Next Time")
        break
    
    




