class normal_calculator:
    def __init__(self):
        self.expression = ""

    def click(self, key, equation):
        if key == "=":
            self.calculate(equation)
            return
        self.expression += str(key)
        equation.set(self.expression)

    def calculate(self, equation):
        try:
            total = str(eval(self.expression))
            equation.set(total)
            self.expression = total
        except:
            equation.set("An error has been detected")
            self.expression = ""

    def delete(self, equation):
        self.expression = ""
        equation.set("")

class advanced_calculator:
    def __init__(self):
        self.expression = ""

    def click(self, key, equation):
        if key == "=":
            self.calculate(equation)
            return
        self.expression += str(key)
        equation.set(self.expression)

    def calculate(self, equation, expression):
        for i in range (len(expression)):


