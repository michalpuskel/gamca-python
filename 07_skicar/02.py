import tkinter
import random

X_MAX, Y_MAX = 800, 600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()

xx, yy = None, None
w = 1
c = 'black'

s = 30


def klik(event):
    x, y = event.x, event.y
    global w, c

    if 0 < x < 2*s and y > Y_MAX-2*s:
        w = 10
        print(f'nastavujem hrubku {w}')
    elif 2*s < x < 4*s and y > Y_MAX-2*s:
        w = 5
        print(f'nastavujem hrubku {w}')
    elif 4*s < x < 6*s and y > Y_MAX-2*s:
        w = 1
        print(f'nastavujem hrubku {w}')
    elif X_MAX-2*s < x < X_MAX and y > Y_MAX-2*s:
        c = 'black'
        print(f'nastavujem farbu {c}')
    elif X_MAX-4*s < x < X_MAX-2*s and y > Y_MAX-2*s:
        c = 'red'
        print(f'nastavujem farbu {c}')
    elif X_MAX-6*s < x < X_MAX-4*s and y > Y_MAX-2*s:
        c = 'green'
        print(f'nastavujem farbu {c}')
    elif X_MAX-8*s < x < X_MAX-6*s and y > Y_MAX-2*s:
        c = 'blue'
        print(f'nastavujem farbu {c}')
    elif X_MAX-2*s < x < X_MAX and y < 2*s:
        canvas.delete('all')
        paleta()
        print('mazem plochu')
    else:
        global xx, yy
        xx, yy = x, y


def tahanie(event):
    x, y = event.x, event.y
    global xx, yy
    if xx and yy:
        canvas.create_line(xx, yy, x, y, width=w, fill=c)
        xx, yy = x, y


def pusti(event):
    global xx, yy
    xx, yy = None, None


def paleta():
    i = 1
    # hrubka ciary
    for x in range(s, 3*2*s, 2*s):
        canvas.create_rectangle(x-s, Y_MAX-2*s, x+s, Y_MAX)
        r = (s - 10) * i
        canvas.create_oval(x-r, Y_MAX-s-r, x+r, Y_MAX-s+r, fill='black')
        i /= 2

    # farby
    # bez pola sa nedaju farby for cyklom :/
    canvas.create_rectangle(X_MAX-2*s, Y_MAX-2*s, X_MAX, Y_MAX, fill='black')
    canvas.create_rectangle(X_MAX-4*s, Y_MAX-2*s, X_MAX-2*s, Y_MAX, fill='red')
    canvas.create_rectangle(X_MAX-6*s, Y_MAX-2*s,
                            X_MAX-4*s, Y_MAX, fill='green')
    canvas.create_rectangle(X_MAX-8*s, Y_MAX-2*s,
                            X_MAX-6*s, Y_MAX, fill='blue')

    # zmaz tlacitko
    canvas.create_rectangle(X_MAX-2*s, 0, X_MAX, 2*s, fill='light gray')
    canvas.create_text(X_MAX-s, s, text='Zmaž')


canvas.bind('<ButtonPress>', klik)
canvas.bind('<Motion>', tahanie)
canvas.bind('<ButtonRelease>', pusti)


paleta()


tkinter.mainloop()
