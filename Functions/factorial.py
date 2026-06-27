def factorial(n):
    
    if n == 0:
        return 1
    
    if n < 0:
        return 'Not Defined'

    fact = 1
    for i in range(1,n+1):
        fact *= i

    return fact

num = int(input("Enter a number : "))
result = factorial(num)

print(f'Factorial of {num} = {result}')
