# -*- coding: utf-8 -*-


class Calculator:

    def __init__(self, first_val, second_val):
        self.first_val = first_val
        self.second_val = second_val
    
    def add(self):
        return self.first_val + self.second_val


if __name__ == "__main__":

    calc = Calculator(2, 3)
    added_val = calc.add()
    prit(added_val)
