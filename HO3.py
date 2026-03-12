import tkinter as nick

window = nick.Tk()
window.title("Simple Calculator")
window.resizable(True, True)
window.configure(bg="lightblue",cursor="arrow")
window.geometry("200x200")

result = nick.Label(window, text="ENTER THE NUMBERS :",bg="lightblue")
result.grid(row=0,column=0,columnspan=2, pady=10)

label1 =  nick.Label(window, text="Enter the 1st number:",bg="lightblue")
label1.grid(row=1,column=0, pady=10)

num1 = nick.Entry(window)
num1.grid(row=1, column=1)

label2 = nick.Label(window, text="Enter the 2nd number:",bg="lightblue")
label2.grid(row=2, column=0, pady=10)

num2 = nick.Entry(window)
num2.grid(row=2, column=1)


def add():
    nick1 = int(num1.get())
    nick2 = int(num2.get())
    result["text"] = "The sum of " + str(nick1) + " and " + str(nick2) + " is " + str(nick1 + nick2)

def subtract():
    ed1 = int(num1.get())
    ed2 = int(num2.get())
    result["text"] = "The difference of " + str(ed1) + " and " + str(ed2) + " is " + str(ed1 - ed2)

def multiply():
    que1 = int(num1.get())
    que2 = int(num2.get())
    result["text"] = "The product of " + str(que1) + " and " + str(que2) + " is " + str(que1 * que2)

def divide():
    kak1 = int(num1.get())
    kak2 = int(num2.get())
    result["text"] = "The product of " + str(kak1) + " and " + str(kak2) + " is " + str(kak1 / kak2)

btn_add = nick.Button(window, text="ADD", command=add,bg="white")
btn_add.grid(row=3, column=0, pady=4)

btn_sub = nick.Button(window, text="SUBTRACT", command=subtract,bg="white")
btn_sub.grid(row=3,column=1, pady=4)

btn_mul = nick.Button(window, text="MULTIPLY", command=multiply,bg="white")
btn_mul.grid(row=4, column=0, pady=4)

btn_div = nick.Button(window, text="DIVIDE", command=divide,bg="white")
btn_div.grid(row=4, column=1, pady=4)

window.mainloop()