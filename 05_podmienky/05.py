import tkinter
from random import randrange, randint

X_MAX, Y_MAX = 400, 300

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()

# ak sa na zaciatku vygeneruju okrajove hodnoty moze to pretiect na -1 || 257
# bonus uloha - najst tuto chybu + opravit

r, g, b = randrange(256), randrange(256), randrange(256)
dr, dg, db = randint(-1, 1), randint(-1, 1), randint(-1, 1)

if (dr == 0 and dr == 0 and dg == 0):
    dg = 1


while True:
    canvas.delete('all')

    farba = f'#{r:02x}{g:02x}{b:02x}'
    canvas.create_rectangle(0, 0, X_MAX, Y_MAX, fill=farba)

    r += dr
    g += dg
    b += db

    if (r <= 0 or r >= 255):
        dr *= -1
    if (g <= 0 or g >= 255):
        dg *= -1
    if (b <= 0 or b >= 255):
        db *= -1

    canvas.update()
    canvas.after(1)


tkinter.mainloop()
