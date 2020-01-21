import tkinter
import random


X_MAX, Y_MAX = 800, 600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()


def krabica(x, y, farba1, farba2, strana=100):
    canvas.create_rectangle(x - strana/2, y - strana/2,
                            x + strana/2, y + strana/2, fill=farba1)
    canvas.create_line(x - strana/2, y - strana/2,
                       x + strana/2, y + strana/2, fill=farba2, width=5)
    canvas.create_line(x + strana/2, y - strana/2,
                       x - strana/2, y + strana/2, fill=farba2, width=5)


def heap(x, y, farba1, farba2, n, strana=100):
    for yy in range(n):
        krabica(x, y - yy * strana, farba1, farba2, strana)


# krabica(200, 100, 'sienna4', 'sandy brown')

heap(100, 500, 'sienna4', 'sandy brown', 5)
heap(300, 500, 'green2', 'OliveDrab1', 3)
heap(500, 500, 'gold2', 'yellow', 4)
heap(700, 500, 'firebrick1', 'firebrick4', 2)


tkinter.mainloop()
