try:
    x = input(str("type your full name: "))
    ans1 = x.split(" ")
except ValueError:
    print("try again")
print(len(ans1))
if len(ans1) == 3:
    print(str(ans1[0])[0]+"."+str(ans1[1])[0]+"."+str(ans1[2])[0]+".")
elif len(ans1)== 2:
    print(str(ans1[0])[0]+"."+str(ans1[1])[0]+".")