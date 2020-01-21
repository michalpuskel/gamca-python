import tkinter
import random

X_MAX, Y_MAX = 800, 600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()

xx, yy = None, None


def klik(event):
    global xx, yy
    xx, yy = event.x, event.y


def tahanie(event):
    x, y = event.x, event.y
    global xx, yy
    if xx and yy:
        canvas.create_line(xx, yy, x, y)
        xx, yy = x, y


def pusti(event):
    global xx, yy
    xx, yy = None, None


canvas.bind('<ButtonPress>', klik)
canvas.bind('<Motion>', tahanie)
canvas.bind('<ButtonRelease>', pusti)

tkinter.mainloop()
