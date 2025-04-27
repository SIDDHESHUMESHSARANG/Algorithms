def Fibonacci(n) :
    if n == 0:
        return 0
    elif n == 1 :
        return 1
    else :
        return Fibonacci(n-1) + Fibonacci(n-2)
    
n = int(input('Enter a number greater than or equal to zero : '))

if n < 0 :
    print('Please enter a positve integer')
else :
    print("Fibonacci Series : ")
    for i in range(n) :
        print(Fibonacci(i),end=' ')