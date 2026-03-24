import tkinter as tk

window = tk.Tk()
window.title("NICKELODIAN")
window.resizable(True,True)
window.configure(bg= "lightblue",cursor= "cross")
window.geometry("520x250")

label = tk.Label(window,text="WELCOME!",anchor="center",font=("Arial", 35),bg="lightblue")
label.pack()

n = tk.Button(window,text="REGISTER",anchor="center",font=("Arial", 18),bg="darkblue",fg="white")
n.pack(padx=10,pady=10)

n2 = tk.Toplevel(window)
n2.title("REGISTER")
n2.geometry("300x200")

label2 = tk.Label(n2, text="You have successfully registered!")
label2.pack(pady=5)

label1 = tk.Label(n2, text="REGISTER")
label1.pack(pady=5)

label1 = tk.Label(n2, text="Username:")
label1.pack(pady=5)

entry_username = tk.Entry(n2)
entry_username.pack(pady=5)

label2 = tk.Label(n2, text="Password:")
label2.pack(pady=5)

entry_password = tk.Entry(n2, show="*")
entry_password.pack(pady=5)

e = tk.Button(n2, text="submit", command=lambda: handle_registration(entry_username.get(), entry_password.get()))
e.pack(pady=5)

n1 = tk.Button(window,text="LOGIN",anchor="center",font=("Arial", 18),bg="green",fg="white")
n1.pack(padx=10,pady=10)

window.mainloop()