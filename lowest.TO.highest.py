while True:
 x=int(input("first number"))
 y=int(input("second number"))
 if x>y:
  for i in range(y,x+1):
   print(i)
 elif y>x:
  for i in range(x,y+1):
   print(i)
 else:
  print("same number")