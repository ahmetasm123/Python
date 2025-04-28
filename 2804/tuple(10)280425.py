x=[]
x1=[]
n="n"
while True:
    y= str(input("writing the letter N will end the process \n give numbers: "))
    if y.lower() !=n.lower():
        x.append(y)
    else:
        break
for i in range(len(x)):
    if int(x[i])<0:
        x1.append(x[i])
print(x1)