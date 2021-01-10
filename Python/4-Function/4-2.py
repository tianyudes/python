import sys
sys.setrecursionlimit(1000)
# Set the maximum Iteration times


def add(a,b):
    return a + b


def print_code(code):
    print(code)
    # no return value.


a = add(2, 3)
b = print_code('python')
# no return value so there will be a None in the output.


print(a,b)

