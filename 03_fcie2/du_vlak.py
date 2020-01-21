import tkinter
import random


X_MAX, Y_MAX = 800, 600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()


def vagon(x, y, farba, dlzka=150):
    a, b = dlzka/2, dlzka/4
    canvas.create_line(x - a - 10, y + b - 10, x + a + 10, y + b - 10, width=5)
    canvas.create_rectangle(x - a, y - b, x + a, y + b, fill=farba)

    r = dlzka/8
    canvas.create_oval(x - b - r, y + b - r,
                       x - b + r, y + b + r, fill='black')
    canvas.create_oval(x + b - r, y + b - r,
                       x + b + r, y + b + r, fill='black')


def vlak(x, y, farba, n, dlzka=150):
    for xx in range(n):
        vagon(x + xx * (dlzka + 20), y, farba)


# vagon(200, 100, 'red')

vlak(100, 100, 'red', 4)
vlak(100, 300, 'green', 2)
vlak(100, 500, 'blue', 3)


tkinter.mainloop()
