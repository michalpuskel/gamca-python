import tkinter
import random


X_MAX, Y_MAX = 800, 600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()


def stvorce(x, y, n, velkost=200, medzera=10):
    strana = velkost
    for _ in range(n):
        canvas.create_rectangle(
            x - strana/2, y - strana/2, x + strana/2, y + strana/2)
        strana -= medzera


for _ in range(100):
    velkost = random.randint(150, 300)
    x = 2 + velkost/2 + random.randrange(X_MAX - velkost - 2)
    y = 2 + velkost/2 + random.randrange(Y_MAX - velkost - 2)
    n = random.randint(5, 10)
    m = random.randint(5, 10)

    stvorce(x, y, n, velkost, m)

tkinter.mainloop()
