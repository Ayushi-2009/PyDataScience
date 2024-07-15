from turtle import *
speed ('fastest')
s = 8
d = 100
for i in range(s):
    fd(d)
    lt(360/s)
    write(i, font = ('Arial', 12 , 'normal'))
    dot(360/s)
mainloop()