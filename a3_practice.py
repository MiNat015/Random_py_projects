import tkinter as tk

WIDTH = 800
HEIGHT = 600
LEVEL_WIDTH = 550
LEVEL_HEIGHT = 500

LEVEL_ROWS = 7
LEVEL_COLUMNS = 8

root = tk.Tk()
root.geometry('800x600')

frame = tk.Frame(root, bg='pink')
frame.pack(expand=tk.TRUE, fill=tk.BOTH)

title_canvas = tk.Canvas(frame, height=80, width=800, bg='light green')
title_canvas.pack(side=tk.TOP)

level_canvas = tk.Canvas(frame, height=LEVEL_HEIGHT, width=LEVEL_WIDTH)
level_canvas.pack(side=tk.LEFT)

inventory_canvas = tk.Canvas(frame, height=500, width=250, bg='light blue')
inventory_canvas.pack(side=tk.RIGHT)


# btn1 = tk.Button(frame2, text='Button1')
# btn1.pack(side=tk.TOP, expand=tk.TRUE)
#
# btn2 = tk.Button(frame2, text='Button2')
# btn2.pack(side=tk.TOP, expand=tk.TRUE)
#
# btn3 = tk.Button(frame, text='Button3')
# btn3.pack(side=tk.LEFT, expand=tk.TRUE)
#
# btn4 = tk.Button(frame, text='Button4')
# btn4.pack(side=tk.LEFT, expand=tk.TRUE)

root.mainloop()
