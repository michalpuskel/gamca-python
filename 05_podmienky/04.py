import tkinter
from random import randrange

X_MAX, Y_MAX = 400, 300

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()

r = 50
x, y = r + randrange(X_MAX - 2*r), r + randrange(Y_MAX - 2*r)
dx, dy = 1, -1

farba = 'blue'

while True:
    canvas.delete('all')
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=farba)

    x += dx
    y += dy

    if (x + r >= X_MAX or x - r <= 0):
        dx *= -1
        # farba = f'#{randrange(256):02x}{randrange(256):02x}{randrange(256):02x}'
    if (y + r >= Y_MAX or y - r <= 0):
        dy *= -1
        # farba = f'#00{randrange(256):02x}00'

    canvas.update()
    canvas.after(1)


tkinter.mainloop()
