while True:
    try:
        score = int(input("Whats the score"))
        exp = int(input("Years of experience"))
        break
    except:
        print("That's not a valid option!")


if  90<=score:
  print("Application succesfull, you can proceed")
elif 70<=score and 5<=exp:
  print("Application succesfull, you can proceed")
elif 70<=score:
  print("Application succesfull, consult needed")
elif 4<=exp:
  print("Application succesfull, consult needed")
else :
    print("Not compatible")