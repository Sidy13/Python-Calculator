import math
class normal_calculator:
    self_mode = 0


    def __init__(self):
        self.expression = ""

    def mode(self):
        mode = 1
        return mode
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
            expression = expression.replace("x²", "**2")
            expression = expression.replace("√", "**0.5")
            expression = expression.replace("sin", "math.sin")
            expression = expression.replace("cos", "math.cos")
            expression = expression.replace("tan", "math.tan")
            expression = expression.replace("arcsin", "math.asin")
            expression = expression.replace("arccos", "math.acos")
            expression = expression.replace("arctan", "math.atan")
            total = str(eval(self.expression))
            equation.set(total)
            self.expression = total
        except:
            equation.set("An error has been detected")
            self.expression = ""

    def delete(self, equation):
        self.expression = ""
        equation.set("")

    def switch_mode(self):
        if self.mode == 0:
            self.mode = 1
            #self.switch_mode_label.config(text="Normal Mode")
            #self.create_advanced_calculator()
        else:
            self.mode = 0
            #self.switch_mode_label.config(text="Advanced Mode")
            #self.create_normal_calculator()
        return self.mode

class advanced_calculator:
    def __init__(self):
        self.expression = ""

    def mode(self):
        mode = 0
        return mode
    def click(self, key, equation, expression):
        if key == "=":
            self.calculate(equation, expression)
            return
        self.expression += str(key)
        equation.set(self.expression)

    def power(self, value, power):
        return value**power

    def n_sqrt(self, value, n):
        return value**(1/n)
    def calculate(self, equation, expression):
        try:
            expression = expression.replace("ln", "math.log")
            expression = expression.replace("e", "math.exp")
            expression = expression.replace("x²", "**2")
            expression = expression.replace("√", "**0.5")
            expression = expression.replace("sin", "math.sin")
            expression = expression.replace("cos", "math.cos")
            expression = expression.replace("tan", "math.tan")
            expression = expression.replace("arcsin", "math.asin")
            expression = expression.replace("arccos", "math.acos")
            expression = expression.replace("arctan", "math.atan")
            total = eval(expression)
            equation.set(total)
            self.expression = str(total)
        except:
            equation.set("An error has been detected")
            self.expression = ""

        def mode(self):
            self.mode = 0
            return self.mode

    def switch_mode(self):
        if self.mode == 0:
            self.mode = 1
            #self.switch_mode_label.config(text="Normal Mode")
            #self.create_advanced_calculator()
        else:
            self.mode = 0
            #self.switch_mode_label.config(text="Advanced Mode")
            #self.create_normal_calculator()
        return self.mode


