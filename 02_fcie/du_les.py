import tkinter
import random

X_MAX, Y_MAX = 800, 600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()


def strom(x, y, r=50):
    canvas.create_line(x, y, x, y+150, width=20, fill='brown4')
    canvas.create_oval(x-r, y-r, x+r, y+r, fill='lawn green')


def trava(x, y):
    for _ in range(random.randint(3, 10)):
        canvas.create_line(x, y,
                           random.randint(x-20, x+20),
                           random.randint(y-30, y-10),
                           width=random.randint(1, 3), fill='green4')


for _ in range(10):
    strom(random.randrange(X_MAX), random.randrange(
        Y_MAX), random.randint(30, 70))
for _ in range(20):
    trava(random.randrange(X_MAX), random.randrange(Y_MAX))


tkinter.mainloop()
