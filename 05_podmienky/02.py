import tkinter
from random import randrange

X_MAX, Y_MAX = 400, 300

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()

r = 50
x, y = r + randrange(X_MAX - 2*r), r + randrange(Y_MAX - 2*r)
dx = 1

while True:
    canvas.delete('all')
    canvas.create_rectangle(x-r, y-r, x+r, y+r, fill='red')

    x += dx

    # if (x > X_MAX):
    #     dx = -1

    # if (x + r > X_MAX):
    #     dx = -1

    # if (x + r >= X_MAX):
    #     dx = -1
    # # pozor ak dx je != 1

    # if (x + r >= X_MAX):
    #     dx = -1
    # if (x - r <= 0):
    #     dx = 1

    if (x + r >= X_MAX or x - r <= 0):
        dx *= -1

    canvas.update()
    canvas.after(1)


tkinter.mainloop()
