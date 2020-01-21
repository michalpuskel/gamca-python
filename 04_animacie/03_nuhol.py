import tkinter
import time
from math import cos, sin, pi

X_MAX, Y_MAX = 800, 600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()


def n_kvet(x, y, n=3, r=50, alpha=0):
    u = 360 / n
    for i in range(n):
        uhol = u * i + alpha
        xx = x + cos(uhol * pi / 180) * r
        yy = y - sin(uhol * pi / 180) * r
        canvas.create_line(x, y, xx, yy)
    canvas.create_oval(x-5, y-5, x+5, y+5)


start = True

phi = 0
r = 55
while True:
    for n in range(1, 7):
        # n_kvet(10 + r + (n-1) * 2*(r + 10), 300, n, r, phi)
        n_kvet(10 + r + (n-1) * 2*(r + 10), 300, n, r, phi * (8 - n))

    phi += 1
    phi %= 360

    if start:
        canvas.update()
        time.sleep(10)
        start = False

    canvas.update()
    canvas.after(100)

tkinter.mainloop()
