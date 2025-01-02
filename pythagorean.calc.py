
while True:
 cx= int(input("start X (1 to 8): "))
 cy= int(input("start Y (1 to 8): "))
 x = int(input("target X (1 to 8): "))
 y = int(input("target Y (1 to 8): "))
 fx=(cx-x)
 fy=(cy-y)
 fx=abs(fx)
 fy=abs(fy)
 xy=fx**2+fy**2
 xy=xy**0.5
 print("distance=" + str(xy))