import tkinter
import time
import random


X_MAX, Y_MAX = 800, 600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()


while True:
    canvas.delete('all')

    for i in range(100):
        x, y = random.randrange(X_MAX), random.randrange(Y_MAX)
        canvas.create_oval(x-5, y-5, x+5, y+5, fill='lightblue')

    canvas.update()
    canvas.after(150)


tkinter.mainloop()
