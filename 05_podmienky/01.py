import tkinter
import random

X_MAX, Y_MAX = 800, 600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()

for _ in range(200):
    x, y = random.randrange(X_MAX), random.randrange(Y_MAX)
    r = 5

    farba = 'black'
    if x > X_MAX / 2:
        farba = 'red'

    # if x > X_MAX / 2:
    #     farba = 'red'
    # else:
    #     farba = 'green'
    #     print('nakreslil sa zeleny stvorcek')

    canvas.create_rectangle(x-r, y-r, x+r, y+r, fill=farba)


tkinter.mainloop()
