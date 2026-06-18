# B.Tech Admission Eligibility Check

name = input("Enter your name: ")
stream = input("Enter your stream in 12th (PCM/PCB/Commerce/Arts): ")

if stream.upper() == "PCM":
    
    percentage_12th = float(input("Enter your 12th percentage: "))
    
    if percentage_12th >= 60:
        
        age = int(input("Enter your age: "))
        
        if age >= 17:
            
            jee_score = int(input("Enter your JEE score (out of 300): "))
            
            if jee_score >= 100:
                print("\nCongratulations", name + "!")
                print("You are eligible for B.Tech admission.")
            else:
                print("\nSorry,", name)
                print("Your JEE score is below the required criteria.")
                
        else:
            print("\nSorry,", name)
            print("Minimum age for admission is 17 years.")
            
    else:
        print("\nSorry,", name)
        print("You need at least 60% in 12th.")
        
else:
    print("\nSorry,", name)
    print("Only PCM students are eligible for B.Tech admission.")