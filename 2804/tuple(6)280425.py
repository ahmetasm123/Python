x=[]
while True:
    try:
        x.append(int(input("writing a letter will end the process \n give numbers: ")))
    except ValueError:
        break
x.sort(reverse=True)
tot=sum(x)
print(tot)
print(x)