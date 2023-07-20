from tkinter import *

ws = Tk()
ws.title("PythonGuides")
ws.geometry("400x300")
ws["bg"] = "#ffbf00"


def printValue():
    a = value_one.get()
    b = value_two.get()
    calc = a + b

    Label(ws, text=f"{calc}, Registered!", pady=20, bg="#ffbf00").pack()


value_one = Entry(ws)
value_two = Entry(ws)
value_one.pack(pady=30)
value_two.pack(pady=30)


Button(ws, text="Register Player", padx=10, pady=5, command=printValue).pack()

ws.mainloop()
