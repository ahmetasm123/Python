def add(st,nd):
    global res
    res = st + nd
def sub(st,nd):
    global res
    res = st - nd
def mul(st,nd):
    global res
    res = st * nd
def div(st,nd):
    global res
    res = st / nd

while True:
 calc= str(input("whats the function= "))
 st= int(input("your first number= "))
 nd= int(input("your second number= "))
 eq="="
 match calc:
  case "+":
      add(st,nd)
      clc = "+"
  case "-":
      sub(st,nd)
      clc = "-"
  case "/":
      div(st,nd)
      clc = "/"
  case "*":
      mul(st,nd)
      clc = "*"
 print(st, clc, nd, eq, res)
