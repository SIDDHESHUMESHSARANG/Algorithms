def factorial(n) :
    if n == 0:
        return 1
    else :
        return n * factorial(n-1)
    
n = int(input('Enter the number greater than or equal to zero : '))
if n >= 0 :
    print(f"{n}! = {factorial(n)}")
else :
    print('Cannot define factorial for a negative number')