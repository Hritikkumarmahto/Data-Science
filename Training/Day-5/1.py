pre_marks = int(input("Enter your prelims marks: "))

if pre_marks >= 300:
    main_marks = int(input("Enter your mains marks: "))

    if main_marks >= 500:
        interview_marks = int(input("Enter your interview marks: "))

        if interview_marks >= 700:
            print("Congrats! You are an IPS officer now.")
        else:
            print("Ohoo! Better luck next time.")
    else:
        print("You have not cleared the mains.")
else:
    print("You have not qualified for the mains exam.")