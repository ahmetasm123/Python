while True:
    try:
        n1 = int(input("first integer: "))
        n2 = int(input("second integer: "))
        n3 = n1 / n2
        print(n3)
        break
    except ValueError:
        print("need integer, try again")
    except ZeroDivisionError:
        print("can't divide by zero")
 #   else:
 #      print("no error")
 # else bloğunu hoca koydu, ama o bloğa asla ulaşılamayak. nedenini anlamadım