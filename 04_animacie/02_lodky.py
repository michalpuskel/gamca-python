import time
import tkinter
import random

X_MAX, Y_MAX = 800, 600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()


def mesiac(x, y, r=50, farba='yellow', pozadie='white'):
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=farba, width=0)
    canvas.create_oval(x - r + 2*r/3,
                       y - r,
                       x + r + 2*r/3,
                       y + r, fill=pozadie, width=0)


def mesiac_obrateny(x, y, r=50, farba='yellow', pozadie='white'):
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=farba, width=0)
    canvas.create_oval(x - r - 2*r/3,
                       y - r,
                       x + r - 2*r/3,
                       y + r, fill=pozadie, width=0)


def logo(x, y, r=50, farba='light sky blue', pozadie='saddle brown'):
    mesiac(x + r + r/10, y, r, farba, pozadie)
    mesiac_obrateny(x - r - r/10, y, r, farba, pozadie)


def vlajka(x, y, farba='darkgreen'):
    a, b = 80, 60
    canvas.create_rectangle(x - a, y - b, x + a, y + b, fill=farba)

    stoziar = 250
    canvas.create_line(x - a, y + b, x - a, y + b + stoziar)

    ostrov_x, ostrov_y = x - a, y + b + stoziar
    ostrov_r = 150
    canvas.create_oval(ostrov_x - ostrov_r, ostrov_y - ostrov_r,
                       ostrov_x + ostrov_r, ostrov_y + ostrov_r, fill='brown')


def lodka(x, y, velkost):
    a, b = 50, 15
    canvas.create_line(x, y, x, y - a * 2 * velkost,
                       width=10 * velkost, fill='brown4')
    canvas.create_polygon(x - a * velkost, y - b * velkost,
                          x + a * velkost, y - b * velkost,
                          x + a/2 * velkost, y + b * velkost,
                          x - a/2 * velkost, y + b * velkost,
                          fill='saddle brown', outline='black', width=2)
    canvas.create_polygon(x, y - a * velkost / 2,
                          x + a * velkost / 2, y - a * 3 * velkost / 4,
                          x, y - a * 2 * velkost, fill='ivory2', outline='black', width=2)
    logo(x, y, 7 * velkost)


r = 40
p = 30
vyska = random.randint(r + p, Y_MAX/2 - r - p)

x1, y1 = 100 + 3 * 100, Y_MAX - 100 * 3
x2, y2 = 100 + 2 * 100, Y_MAX - 100 * 2
x3, y3 = 100 + 1 * 100, Y_MAX - 100 * 1
dx1, dx2, dx3 = 1, 2, 3

start = True

while True:
    canvas.delete('all')

    vlajka(200, 100)
    mesiac(200, 100, 30, 'red', 'darkgreen')

    vlajka(X_MAX - 100, 100, 'red3')
    logo(X_MAX - 100, 100, 20, pozadie='red3')

    canvas.create_rectangle(0, Y_MAX / 2, X_MAX+2, Y_MAX+2, fill='navy')

    mesiac(500, Y_MAX/2 - vyska, r)
    mesiac(500, Y_MAX/2 + vyska, r, pozadie='navy')

    lodka(x1, y1, 1)
    lodka(x2, y2, 2)
    lodka(x3, y3, 3)

    x1 += dx1
    x2 += dx2
    x3 += dx3

    if start:
        canvas.update()
        time.sleep(10)
        start = False

    canvas.update()
    canvas.after(10)


tkinter.mainloop()
