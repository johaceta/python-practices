# implement a function called compose that takes an arbitrary number of functions as its arguments. It should return a new function that represents 
# the composition of functionList[1],functionList[2],functionList[3],...functionList[n] such that the arguments given to the function returned by compose
# are passed to functiionsList[1], the output obtained is passed to functionList[2], and so on. Finally the output of the last function should be returned.

# The functions are

# add(*args) takes a variable number of arguments and returns the sum of the arguments.
# square(a) takes a number as an argument and returns the square of a
# splitter(a) takes a number as an argument, divides the number by 2 and returns a list of length 2:[floor of division, a -floor of division]
# my_max(a) takes a number or list of numbers as an argument and returns the maximum value
# my_min(a) takes a number or list of numbers as an argument and returns the minimum value 

from typing import Callable

def compose(*functionList: Callable):
    # Return a function that represents the composition of functions
    def composed_function(*args):
        # Apply the first function in the functionList with the original arguments
        result = functionList[0](*args)
        # Apply the remaining functions in the functionList one by one
        for func in functionList[1:]:
            result = func(result)
        return result
    return composed_function

# Example functions as given in the problem
def add(*args):
    return sum(args)

def square(a):
    return a * a

def splitter(a):
    floor_division = a // 2
    return [floor_division, a - floor_division]

def my_max(a):
    if isinstance(a, list):
        return max(a)
    return a

def my_min(a):
    if isinstance(a, list):
        return min(a)
    return a

# Input / Output Code
if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    functionMapper = {
        "add": add,
        "square": square,
        "splitter": splitter,
        "my_max": my_max,
        "my_min": my_min,
    }

    functionsList_count = int(input().strip())

    functionsList = []

    for _ in range(functionsList_count):
        functionsList_item = input()
        functionsList.append(functionMapper[functionsList_item])

    composedFunctions = compose(*functionsList)

    argumentsList_count = int(input().strip())

    argumentsList = []

    for _ in range(argumentsList_count):
        argumentsList_item = int(input().strip())
        argumentsList.append(argumentsList_item)

    result = composedFunctions(*argumentsList)

    fptr.write(str(result) + "\n")

    fptr.close()
