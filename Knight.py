
while True:
 cx= int(input("knight X (1 to 8): "))
 cy= int(input("knight Y (1 to 8): "))
 x = int(input("target X (1 to 8): "))
 y = int(input("target Y (1 to 8): "))
 fx=(cx-x)
 fy=(cy-y)
 if fx < 0:
  fx= -fx
 if fy < 0:
  fy=-fy
 if 8>=x and 8>=y and 8>=cx and 8>=cy:
  if (fx==2 and fy==1) or (fx==1 and fy==2):
    print("can move")
  else:
    print("can't move")
 else:
  print("outside of the board")
