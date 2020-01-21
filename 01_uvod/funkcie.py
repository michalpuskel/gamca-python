import tkinter

canvas = tkinter.Canvas(width=600, height=600)
canvas.pack()

sx = 300
sy = 300
r = 50
canvas.create_oval(sx + r, sy + r, sx - r, sy - r)

tkinter.mainloop()
