import math


def bar(val, max_val, symbol):
    max_symbols = 30
    curr = math.ceil((val / max_val) * max_symbols)
    empty = max_symbols - curr
    bar = "|" + symbol * curr + " " * empty + "|"
    return bar


def string3(one, two, three):
    return one.ljust(18) + " " + two.ljust(7) + " " + three