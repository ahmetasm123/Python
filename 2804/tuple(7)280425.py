x=[]
n="n"
while True:
    y= str(input("writing the letter N will end the process \n give numbers: "))
    if y.lower() !=n.lower():
        x.append(y)
    else:
        break

x.sort(reverse=True)
for i in range(len(x)):
    print(f"Indeks: {i}, Element: {x[i]}")
print(x)