x=[]
x1=[]
n="n"
while True:
    y= str(input("writing the letter N will end the process \n give numbers: "))
    if y.lower() !=n.lower():
        x.append(y)
    else:
        break
for i in range(1,len(x)):
    if x[i]>x[i-1]:
        x1.append(x[i])
print(x1)