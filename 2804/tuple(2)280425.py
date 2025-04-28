x1=int(input("1st object, X coordinate: "))
y1=int(input("1st object, Y coordinate: "))
x2=int(input("2nd object, X coordinate: "))
y2=int(input("2nd object, Y coordinate: "))
O1=(x1,y1)
O2=(x2,y2)
if O1[0] > O2[0]:
    rsX = O1[0] - O2[0]
elif O1[0] < O2[0]:
    rsX = O2[0] - O1[0]
if O1[1] > O2[1]:
    rsY = O1[1] - O2[1]
elif O1[1] < O2[1]:
    rsY = O2[1] - O1[1]
top=((rsX**2)+(rsY**2))
top=top**0.5
print("distance in X: "+f"{rsX:.2f}\n"+"distance in Y: "+f"{rsY:.2f}\n"+"calculated distance: "+f"{top:.2f}\n")