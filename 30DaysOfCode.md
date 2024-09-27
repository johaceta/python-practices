day 0 Print "Hello, World" and the content of a given input_string 

print(f"Hello, World.\n{input_string}")

*day 1 - data types*
i = 4
d = 4.0
s = 'HackerRank '

Declare second integer, double, and String variables. Read and save an integer, double, and String to your variables. 
Print the sum of both integer variables on a new line.
Print the sum of the double variables on a new line.
Concatenate and print the String variables on a new line
The 's' variable above should be printed first.

intInput = int(input())
floatInput = float(input())
StringInput = float(input())

print(i+intInput)
print(d+floatInput)
print(s+StringInput)

Another way to print it print(f"{i+intInput}\n{d+floatInput}\n{s+StringInput}")

*day 2 - Operators*

Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. Round the result to the nearest integer.

def solve(meal_cost, tip_percent, tax_percent):
    tip_value = (tip_percent / 100) * meal_cost
    tax_value = (tax_percent / 100) * meal_cost
    total_cost = round(meal_cost + tip_value + tax_value)
    print(total_cost)

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
