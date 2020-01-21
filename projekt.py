import tkinter
from random import randint
from math import sin, cos, pi

X_MAX, Y_MAX = 800, 600

c = tkinter.Canvas(width=X_MAX, height=Y_MAX)
c.pack()


hodiny, minuty, sekundy = 10, 50, randint(0, 59)
rychlost = 3

sx, sy = X_MAX/2, Y_MAX/2
r = min(sx, sy) - 50

uhol = 360 / 12
posun = 2


def kresli():
    c.delete('all')

    c.create_oval(sx-r, sy-r, sx+r, sy+r)

    global sekundy, minuty, hodiny, rychlost

    # minuty
    for u in range(0, 360, 360//12//5):
        x1 = sx + cos(u * pi / 180) * r
        y1 = sy - sin(u * pi / 180) * r
        x2 = sx + cos(u * pi / 180) * (r - 10)
        y2 = sy - sin(u * pi / 180) * (r - 10)
        c.create_line(x1, y1, x2, y2)

    # hodiny
    for u in range(12):
        x = sx + cos(uhol * (posun - u) * pi / 180) * (r - 30)
        y = sy - sin(uhol * (posun - u) * pi / 180) * (r - 30)
        c.create_text(x, y, text=u+1, font='Courier 24')

        x1 = sx + cos(uhol * (posun - u) * pi / 180) * r
        y1 = sy - sin(uhol * (posun - u) * pi / 180) * r
        x2 = sx + cos(uhol * (posun - u) * pi / 180) * (r - 10)
        y2 = sy - sin(uhol * (posun - u) * pi / 180) * (r - 10)
        c.create_line(x1, y1, x2, y2, width=5)

    # hodinova rucicka
    u_hod = (hodiny + minuty / 60) * 360//12 - 90
    x_hod = sx + cos(-u_hod * pi / 180) * (r - 70)
    y_hod = sy - sin(-u_hod * pi / 180) * (r - 70)
    c.create_line(sx, sy, x_hod, y_hod, width=7)

    # minutova rucicka
    u_min = minuty * 360//12//5 - 90
    x_min = sx + cos(-u_min * pi / 180) * (r - 20)
    y_min = sy - sin(-u_min * pi / 180) * (r - 20)
    c.create_line(sx, sy, x_min, y_min, width=3)

    # sekundova rucicka
    u_sek = sekundy * 360//12//5 - 90
    x_sek = sx + cos(-u_sek * pi / 180) * (r - 15)
    y_sek = sy - sin(-u_sek * pi / 180) * (r - 15)
    if rychlost == 1:
        farba = 'red'
    elif rychlost == 2:
        farba = 'orange'
    elif rychlost == 3:
        farba = 'chartreuse'
    elif rychlost == 4:
        farba = 'deepskyblue2'
    c.create_line(sx, sy, x_sek, y_sek, fill=farba)

    # logika pocitania hodin
    sekundy += 1

    if sekundy >= 60:
        minuty += 1

    if minuty >= 60:
        hodiny += 1

    sekundy %= 60
    minuty %= 60
    hodiny %= 12

    if rychlost == 1:
        pauza = 1000
    elif rychlost == 2:
        pauza = 500
    elif rychlost == 3:
        pauza = 100
    elif rychlost == 4:
        pauza = 1

    c.update()
    c.after(pauza)


def zrychli(event):
    global rychlost
    if rychlost < 4:
        rychlost += 1


def spomal(event):
    global rychlost
    if rychlost > 1:
        rychlost -= 1


c.bind('<Button-1>', zrychli)
c.bind('<Button-2>', spomal)


while True:
    kresli()


tkinter.mainloop()
