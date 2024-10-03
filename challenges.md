Given an integer, n, perform the following conditional actions:

If n is odd, print Weird 
If n is even and in the inclusive range of 2 to 5 , print Not Weird 
If  n is even and in the inclusive range of  6to 20, print Weird 
If n is even and greater than 20, print Not Weird" 


n = int(input().strip())
if (n % 2 != 0):
    print('Weird')
elif (n % 2 == 0) and (n in range(2, 6)):
    print('Not Weird')
elif (n % 2 == 0) and (n in range(6, 21)):
    print('Weird')
elif (n % 2 == 0) and (n > 20):
    print('Not Weird')


An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
    The year can be evenly divided by 100, it is NOT a leap year, unless:
        The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

def is_leap(year):
    leap = False
    if (year % 4 == 0):
        if (year % 100 == 0): # if it's no evenly divisible by 100 then is a common leap year
            if (year % 400 == 0):
                leap = True
        else:
            leap = True
    return leap

year = int(input())
print(is_leap(year))


given an integer n, without using any string methods, try to print the following: 123

n = int(input())
for i in range(1, n + 1):
    print(i, end='') # end='' Print numbers without a newline

Check if a string is palindrome 

 slicing syntax is sequence[start:stop:step]
 [::-1] means: Start at the end (the minus does that for you), end when nothing's left and walk backwards by 1.
 
def palindrome(str_word):
    reservedWord = str_word[::-1].lower()
    if (str_word.lower() == reservedWord):
        return True
    else:
        return False


userInput = input()
isPalindrome = palindrome(userInput)
print(isPalindrome)

