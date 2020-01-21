import tkinter
import time
from math import cos, sin, pi

X_MAX, Y_MAX = 800, 600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()


def draha():
    stare_x = -X_MAX/2

    # stare_y = Y_MAX/2 - stare_x/2
    # stare_y = Y_MAX/2 - (stare_x/24) ** 2
    stare_y = Y_MAX/2 + sin(stare_x * pi / 180) * 200

    for x in range(round(-X_MAX/2), round(X_MAX/2)):

        # y = Y_MAX/2 - x/2
        # y = Y_MAX/2 - (x/24) ** 2
        y = Y_MAX/2 + sin(x * pi / 180) * 200

        xx = X_MAX/2 + x
        canvas.create_line(stare_x, stare_y, xx, y)
        stare_x, stare_y = xx, y


start = True

for x in range(round(-X_MAX/2), round(X_MAX/2)):
    canvas.delete('all')
    draha()

    # y = Y_MAX/2 - x/2
    # y = Y_MAX/2 - (x/24) ** 2
    y = Y_MAX/2 + sin(x * pi / 180) * 200

    xx = X_MAX/2 + x
    canvas.create_oval(xx-5, y-5, xx+5, y+5, fill='red')

    if start:
        canvas.update()
        time.sleep(10)
        start = False

    canvas.update()
    canvas.after(50)


tkinter.mainloop()
