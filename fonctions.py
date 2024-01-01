import math
from tkinter import *
class calculator:

    def __init__(self):
        self.expression = ""
        self.mode = 0

    def click(self, key, equation, expression):
        if key == "=":
            self.calculate(equation, expression)
            return
        self.expression += str(key)
        equation.set(self.expression)

    def calculate(self, equation, expression):
        try:
            expression = expression.replace("ln", "math.log")
            expression = expression.replace("e", "math.exp")
            expression = expression.replace("²", "**2")
            expression = expression.replace("√", "math.sqrt")
            expression = expression.replace("sin", "math.sin")
            expression = expression.replace("cos", "math.cos")
            expression = expression.replace("tan", "math.tan")
            expression = expression.replace("arcsin", "math.asin")
            expression = expression.replace("arccos", "math.acos")
            expression = expression.replace("arctan", "math.atan")
            expression = expression.replace("π", "math.pi")
            if "ᴺ" in expression:
                power = int(input())
                expression = expression.replace("ᴺ", f"**{power}")
            total = str(eval(expression, {"__builtins__": None}, {"math": math}))
            equation.set(total)
            expression = total

        except:
            equation.set("An error has been detected")
            expression = ""

    def delete(self, equation):
        self.expression = ""
        equation.set("")

    def radian(self, equation):
            angle = float(equation.get())
            radian = math.radians(angle)
            return equation.set(str(radian))

    def switch_mode(self, gui):
        if self.mode == 0:
            self.mode = 1
        else:
            self.mode = 0
        gui.destroy()
        self.gui()

    def gui(self):
        gui = Tk()
        if self.mode == 0:
            self.normal_calculator(gui)
            gui.geometry("235x457")
        else:
            self.advanced_calculator(gui)
            gui.geometry("300x670")
        gui.configure(background="#101419")
        gui.title("Py Calculator")
        gui.mainloop()

    def normal_calculator(self, gui):

        equation = StringVar()
        # Results
        results = Label(gui, bg="#101419", fg="#FFF", textvariable=equation, height=2)
        results.grid(columnspan=4)

        # Buttons
        buttons = [7, 8, 9, "+", 4, 5, 6, "-", 1, 2, 3, "*", 0, ".", "/", "="]
        row = 1
        column = 0
        for i in buttons:
            b = Label(gui, text=str(i), bg="#476C9B", fg="#FFF", height=4, width=6)
            b.bind("<Button-1>", lambda e, i=i: self.click(i, equation, self.expression))
            b.grid(row=row, column=column)
            column += 1
            if column == 4:
                column = 0
                row += 1

        d = Label(gui, text="Delete", bg="#984447", fg="#FFF", height=4, width=26)
        d.bind("<Button-1>", lambda e: self.delete(equation))
        d.grid(columnspan=5)

        c = 0
        a = Label(gui, text="Advanced Mode", bg="#2ECC71", fg="#FFF", height=4, width=26)
        a.grid(columnspan=5)
        a.bind("<Button-1>", lambda e: self.switch_mode(gui))

    def advanced_calculator(self, gui):
        equation = StringVar()
        results = Label(gui, bg="#101419", fg="#FFF", textvariable=equation, height=2)
        results.grid(columnspan=4)

        # Buttons
        buttons = ["ln", 7, 8, 9, "+", "e", 4, 5, 6, "-", "²", 1, 2, 3, "*", "√", 0, ".", "/", "=", "ᴺ", "cos", "sin",
                   "tan", "π", "(", "arccos", "arcsin", "arctan", ")"]
        row = 1
        column = 0
        for i in buttons:
            b = Label(gui, text=str(i), bg="#476C9B", fg="#FFF", height=4, width=6)
            b.bind("<Button-1>", lambda e, i=i: self.click(i, equation, self.expression))
            b.grid(row=row, column=column)
            column += 1
            if column == 5:
                column = 0
                row += 1

        r = Label(gui, text="Radian", bg="#FFC0CB", fg="#FFF", height=4, width=32)
        r.bind("<Button-1>", lambda e: self.radian(equation))
        r.grid(columnspan=5)


        d = Label(gui, text="Delete", bg="#984447", fg="#FFF", height=4, width=32)
        d.bind("<Button-1>", lambda e: self.delete(equation))
        d.grid(columnspan=5)

        a = Label(gui, text="Normal mode", bg="#2ECC71", fg="#FFF", height=4, width=32)
        a.grid(columnspan=5)
        a.bind("<Button-1>", lambda e: self.switch_mode(gui))











