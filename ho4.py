import tkinter as tk

window = tk.Tk()
window.title("PROFILE BUILDER")
window.geometry("700x300")
window.configure(bg="lightblue")

# Title Label (at the top)
title_label = tk.Label(window, text="PROFILE BUILDER", bg="lightblue", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# First Name Section
lbl_first = tk.Label(window, text="First Name:", bg="lightblue")
lbl_first.grid(row=1, column=0, padx=10, pady=5, sticky="e")
ent_first = tk.Entry(window)
ent_first.grid(row=1, column=1, padx=10, pady=5)

# Middle Name Section
lbl_middle = tk.Label(window, text="Middle Name:", bg="lightblue")
lbl_middle.grid(row=2, column=0, padx=10, pady=5, sticky="e")
ent_middle = tk.Entry(window)
ent_middle.grid(row=2, column=1, padx=10, pady=5)

# Last Name Section
lbl_last = tk.Label(window, text="Last Name:", bg="lightblue")
lbl_last.grid(row=3, column=0, padx=10, pady=5, sticky="e")
ent_last = tk.Entry(window)
ent_last.grid(row=3, column=1, padx=10, pady=5)

window.mainloop()
