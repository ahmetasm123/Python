acc= 1000
while True:
 print("your accounts balance is=" + str(acc))
 y=str(input("Would you like to deposit or withdraw(lower case only)"))
 if y in ["deposit","withdraw"]:
    print("proceding...")
    if y in ["deposit"]:
        h=int(input("Please enter the amount deposited"))
        acc= h+acc
    elif y in ["withdraw"]:
        j=int(input("Please enter the amount withdrawn"))
        if j>acc:
            print("You can't withdraw more than your balance")
            continue
        elif acc>=j:
            acc=acc-j
    print("successfull transaction")
    print("current balance is=" + str(acc))
 else :
    print("please type a correct action")