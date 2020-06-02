#學號:50601102
#姓名:許展銘
import turtle
t=turtle.Turtle()
n=int(input('邊數==>'))
l=int(input('邊長==>'))

for x in range(n):
    t.forward(l)
    t.right(360/n)
