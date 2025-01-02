import turtle
import time
turtle=turtle.Turtle()
turtle.speed(10)
num=int(input("whats the size"))
for i in range(4):
 turtle.forward(num)
 turtle.right(90)
turtle.left(60)
for i in range(2):
 turtle.forward(num)
 turtle.right(120)
time.sleep(10)