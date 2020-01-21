import tkinter
from math import cos, sin, pi

X_MAX, Y_MAX = 800, 600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()


def n_kvet(x, y, n=3, r=50):
    u = 360 / n
    for i in range(n):
        uhol = u * i
        xx = x + cos(uhol * pi / 180) * r
        yy = y - sin(uhol * pi / 180) * r
        canvas.create_line(x, y, xx, yy)
    canvas.create_oval(x-5, y-5, x+5, y+5)


r = 55
for n in range(1, 7):
    n_kvet(r + (n-1) * 2*(r + 10), 300, n, r)

tkinter.mainloop()
