x=[]
y=[]
while True:
    try:
        x.append(int(input("writing a letter will end the process \n give numbers: ")))
    except ValueError:
        break
x.sort(reverse=True)
for i in x:
    if i%2==0:
        y.append(i)
    else:
        continue
print(y)
