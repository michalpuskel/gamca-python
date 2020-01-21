import tkinter
import random

X_MAX, Y_MAX = 800, 600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()

hrac_a, hrac_b = 50, 10
hrac_x, hrac_y = X_MAX / 2, Y_MAX - hrac_b


def pohyb(event):
    global hrac_x
    hrac_x = event.x

    canvas.delete('all')

    canvas.create_rectangle(hrac_x - hrac_a, hrac_y - hrac_b,
                            hrac_x + hrac_a, hrac_y + hrac_b, fill='blue')

    # canvas.update()
    # canvas.after(100)


canvas.bind('<Motion>', pohyb)

x, y, = 100, 100
r = 50

while True:
    print('ok')
    print(hrac_x)

    canvas.create_oval(x-r, y-r, x+r, y+r)

    x += 10

    canvas.update()
    canvas.after(100)

    print(hrac_x)


tkinter.mainloop()
