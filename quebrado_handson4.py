import tkinter as tk

window = tk.Tk()

nick_label = tk.Label(window,text="simple calculator")
nick_label.grid()

nick1_label = tk.Label(window,text="Enter 1st number")
nick1_label.grid(row=0,)

nick1_entry = tk.Entry(window)
nick1_entry.grid()

nick1_label = tk.Label(window,text="Enter 2nd number")
nick1_label.grid()

nick1_entry = tk.Entry(window)
nick1_entry.grid()

button = tk.Button(window,text="ADD")
button.grid()

button = tk.Button(window,text="multiply")
button.grid()

button = tk.Button(window,text="subtract")
button.grid()

button = tk.Button(window,text="division")
button.grid()




window.mainloop()

