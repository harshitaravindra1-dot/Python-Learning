def prime(n):
    
    if n <= 0:
        print(f"{n} is not a prime number ")
        
    count = 0
    for i in range(2,n):
        if n % i == 0:
            count += 1

    if count == 0:
        print(f"{n} is a prime number")

    else:
        print(f'{n} is not a prime number')

num = int(input("Enter a number : "))
prime(num)

