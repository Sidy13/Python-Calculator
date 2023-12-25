from tkinter import *
from fonctions import *

#Noir = #101419
#Bleu = #476C9B
#Rouge = #984447

expression = ""

mode = 0

if __name__ == "__main__":
    gui = Tk()

    # Background color
    gui.configure(background="#101419")

    # Title
    gui.title("Py Calculator")

    while mode == 0:
        # Window
        gui.geometry("235x457")

        # Values equation
        equation = StringVar()

        calculator = normal_calculator()

        # Results
        results = Label(gui, bg="#101419", fg="#FFF", textvariable=equation, height=2)
        results.grid(columnspan=4)

        # Buttons
        buttons = [7, 8, 9, "+", 4, 5, 6, "-", 1, 2, 3, "*", 0, ",", "/", "="]
        row = 1
        column = 0
        for i in buttons:
            b = Label(gui, text=str(i), bg="#476C9B", fg="#FFF", height=4, width=6)
            b.bind("<Button-1>", lambda e, i=i: calculator.click(i, equation))
            b.grid(row=row, column=column)
            column += 1
            if column == 4:
                column = 0
                row += 1

        d = Label(gui, text="Delete", bg="#984447", fg="#FFF", height=4, width=26)
        d.bind("<Button-1>", lambda e: calculator.delete(equation))
        d.grid(columnspan=5)

        a = Label(gui, text="Advanced Mode", bg="#2ECC71", fg="#FFF", height=4, width=26)
        a.grid(columnspan=5)
        a.bind("<Button-1>", lambda e: calculator.advanced_mode())

    while mode == 1:
        # Window
        gui.geometry("235x590")

        # Values equation
        equation = StringVar()

        calculator = advanced_calculator()

        # Results
        results = Label(gui, bg="#101419", fg="#FFF", textvariable=equation, height=2)
        results.grid(columnspan=4)

        # Buttons
        buttons = ["ln", 7, 8, 9, "+", "e", 4, 5, 6, "-", "x²", 1, 2, 3, "*", "xᴺ", 0, ",", "/", "=", "√", "cos", "sin",
                   "tan", "π", "ᴺ√", "arccos", "arcsin", "arctan", "10ᴺ"]
        row = 1
        column = 0
        for i in buttons:
            b = Label(gui, text=str(i), bg="#476C9B", fg="#FFF", height=4, width=6)
            b.bind("<Button-1>", lambda e, i=i: calculator.click(i, equation))
            b.grid(row=row, column=column)
            column += 1
            if column == 4:
                column = 0
                row += 1

        d = Label(gui, text="Delete", bg="#984447", fg="#FFF", height=4, width=26)
        d.bind("<Button-1>", lambda e: calculator.delete(equation))
        d.grid(columnspan=5)

        a = Label(gui, text="Normal", bg="#2ECC71", fg="#FFF", height=4, width=26)
        a.grid(columnspan=5)
        a.bind("<Button-1>", lambda e: calculator.advanced_mode())




        gui.mainloop()