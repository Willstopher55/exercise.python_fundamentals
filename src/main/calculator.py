# Created by Leon Hunter at 9:54 AM 10/23/2020
class Calculator(object):
    def add(self, a, b):
        return a + b  # TODO - Implement solution

    def subtract(self, a, b):
        return a - b  # TODO - Implement solution

    def multiply(self, a, b):
        return a * b  # TODO - Implement solution

    def divide(self, a, b):
        # TODO - Implement solution
        x = a / b
        # if b == 0:
        #     x = 0
        # else:
        #     x = round(x, 3)
        # return x

        try:
            x = round(x, 3)
        except ZeroDivisionError:
            x = 0
        return x

