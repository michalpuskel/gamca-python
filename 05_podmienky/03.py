import tkinter
import random

X_MAX, Y_MAX = 800, 600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()

for _ in range(200):
    x, y = random.randrange(X_MAX), random.randrange(Y_MAX)
    r = 5

    farba = 'black'

    # if y > Y_MAX / 2:
    #     farba = 'red'
    # else:
    #     if x < X_MAX / 2:
    #         farba = 'green'
    #     else:
    #         farba = 'blue'

    # if y > Y_MAX / 2:
    #     if x > X_MAX / 2:
    #         farba = 'red'
    #     else:
    #         farba = 'yellow'
    # else:
    #     if x < X_MAX / 2:
    #         farba = 'green'
    #     else:
    #         farba = 'blue'

    # if y > Y_MAX / 2 and x > X_MAX / 2:
    #     farba = 'red'
    # else:
    #     if y > Y_MAX / 2 and not (x > X_MAX / 2):
    #         # if y > Y_MAX / 2 and x <= X_MAX / 2:
    #         farba = 'yellow'
    #     else:
    #         if y <= Y_MAX / 2 and x > X_MAX / 2:
    #             farba = 'green'
    #         else:
    #             if y <= Y_MAX / 2 and x <= X_MAX / 2:
    #                 farba = 'blue'
    #             else:
    #                 print('prave sa stalo NEMOZNE')

    if y > Y_MAX / 2 and x > X_MAX / 2:
        farba = 'red'
    elif y > Y_MAX / 2 and x <= X_MAX / 2:
        farba = 'yellow'
    elif y <= Y_MAX / 2 and x > X_MAX / 2:
        farba = 'green'
    elif y <= Y_MAX / 2 and x <= X_MAX / 2:
        farba = 'blue'
    else:
        print('prave sa stalo NEMOZNE')

    canvas.create_rectangle(x-r, y-r, x+r, y+r, fill=farba)


tkinter.mainloop()
