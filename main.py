from tkinter import *

#Noir = #101419
#Bleu = #476C9B
#Rouge = #984447

expression = ""

def click (key):
    if key == "=":
        calculate()
        return

    global expression
    expression += str(key)
    equation.set(expression)

def calculate():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("An error has been detected")
        expression=""


def delete():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = Tk()

    # Background color
    gui.configure(background="#101419")

    # Title
    gui.title("Py Calculator")

    # Window
    gui.geometry("235x385")

    # Values equation
    equation = StringVar()

    # Results
    results = Label(gui, bg="#101419", fg="#FFF", textvariable=equation, height = 2)
    results.grid(columnspan=4)

    # Buttons
    buttons = [7, 8, 9, "*", 4, 5, 6, "-", 1, 2, 3, "+", 0, ",", "/", "="]
    row = 1
    column = 0
    for i in buttons:
        b = Label(gui, text=str(i), bg="#476C9B", fg="#FFF", height= 4, width = 6)
        b.bind("<Button-1>", lambda e, i = i: click(i))
        b.grid(row=row, column= column)
        column += 1
        if column==4:
            column = 0
            row += 1

    b = Label(gui, text="Delete", bg="#984447", fg="#FFF", height=4, width=26)
    b.bind("<Button-1>", lambda e: delete())
    b.grid(columnspan=4)

    gui.mainloop()
