x=[]
while True:
    try:
        x.append(int(input("writing a letter will end the process \n give numbers: ")))
    except ValueError:
        break
x.sort(reverse=True)
print(f"{x[0]} is the highest number input \n")
print(x)