while True:
 calc= str(input("whats the function= "))
 st= int(input("your first number= "))
 nd= int(input("your second number= "))
 eq="="
 match calc:
  case "+":
      res = st + nd
      clc = "+"
  case "-":
      res = st - nd
      clc = "-"
  case "/":
      res = st / nd
      clc = "/"
  case "*":
      res = st * nd
      clc = "*"
 print(st, clc, nd, eq, res)