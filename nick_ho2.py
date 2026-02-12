import tkinter as tk

window = tk.Tk()

window.title("MY PROFILE")
window.geometry("600x600")
window.resizable(True,True)
window.configure(bg="lightblue",cursor="cross")

label = tk.Label(window,text="MY PROFILE",font=("poppins",25),fg="black",bg="lightblue",anchor="center")
label.pack(padx=5,pady=20)

label = tk.Label(window,text="Name : NICK EDERZON M. QUEBRADO",font=("poppins",10),fg="black",bg="lightblue",anchor="center")
label.pack(anchor="w",pady=20)

label = tk.Label(window,text="Age : 19 years old",font=("poppins",10),fg="black",bg="lightblue",anchor="center")
label.pack(anchor="w",pady=20)

label = tk.Label(window,text="Course : BSIT",font=("poppins",10),fg="black",bg="lightblue",anchor="center")
label.pack(anchor="w",pady=20)

label = tk.Label(window,text="Birthday : May 27,2006",font=("poppins",10),fg="black",bg="lightblue",anchor="center")
label.pack(anchor="w",pady=20)

label = tk.Label(window,text="Motto :",font=("poppins",10),fg="black",bg="lightblue",anchor="center")
label.pack(anchor="w",pady=20)

label = tk.Label(window,text="Never stop growing",font=("poppins",10),fg="black",bg="lightblue",anchor="center")
label.pack(padx=5,pady=20)

window.mainloop()