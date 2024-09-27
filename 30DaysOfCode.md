day 0 Print "Hello, World" and the content of a given input_string 

print(f"Hello, World.\n{input_string}")

day 1 - data types 
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
