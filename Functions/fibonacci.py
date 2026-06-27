def fibonacci(n):
    if n < 0:
        print("Please enter a non-negative number.")
    if n == 0:
        print("Fibonacci series:\n0")

    elif n == 1:
        print("Fibonacci series:\n0")
    
    else:
        num_1 = 0
        num_2 = 1
        print(f'Fibonacci series of {n}:')
        print(f'{num_1}\n{num_2}')
        for i in range(2,n):
            num_3 = num_1 + num_2
            print(num_3)
            num_1 = num_2
            num_2 = num_3
        
num = int(input("enter a number : "))
fibonacci(num)
