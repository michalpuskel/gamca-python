import tkinter
import random

X_MAX, Y_MAX = 800, 600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()


def tahanie(event):
    x, y = event.x, event.y
    r = 10
    canvas.create_oval(x-r, y-r, x+r, y+r, fill='red')
    canvas.create_oval(X_MAX - x-r, y-r, X_MAX - x+r, y+r, fill='green')


canvas.bind('<Motion>', tahanie)

tkinter.mainloop()
