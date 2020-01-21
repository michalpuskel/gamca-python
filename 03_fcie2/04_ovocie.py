import tkinter
import random


X_MAX, Y_MAX = 800, 600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()


def strom(x, y, farba, velkost=150):
    canvas.create_line(x, y, x, y + velkost*2, width=25, fill='saddle brown')
    canvas.create_rectangle(x - velkost/2, y - velkost/2,
                            x + velkost/2, y + velkost/2,
                            fill='lawn green')
    # plody mozu byt tiez vo fcii
    for _ in range(random.randint(5, 10)):
        r = 10
        xx = random.randint(x - velkost // 2 + r, x + velkost // 2 - 2*r)
        yy = random.randint(y - velkost // 2 + r, y + velkost // 2 - 2*r)
        canvas.create_oval(xx - r, yy - r, xx + r, yy + r,
                           fill=farba)


strom(150, 100, 'deep pink', random.randint(100, 200))
strom(400, 200, 'medium blue')
strom(650, 150, 'red2', random.randint(100, 200))

tkinter.mainloop()
