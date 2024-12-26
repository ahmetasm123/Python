while True:
    try:
        age = int(input("Whats the age"))
        score = int(input("Whats the score"))
        break
    except:
        print("That's not a valid option!")

if 20 <= age <= 50 and 80<=score :
    print("Criteria met")
else :
    print("Not compatible")