#學號:50601102
#姓名:許展銘
import turtle
turtle.width(4) #筆深
colors=['blue','black','red','yellow','green']
x=[-120,0,120,-60,60]
y=[0,0,0,-60,-60]
#運行數
for i in range(10):
    for j in range(5):
        turtle.color(colors[j]) #筆色彩
        turtle.up()
        turtle.setpos(x[j],y[j]) #筆位置
        turtle.down()
        turtle.circle(80) #圓大小
        x[j]=x[j]+10

