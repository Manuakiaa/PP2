"""Asman is very curious and likes to check whether some numberis prime or not. Check if the number is prime.
A prime number is a number that has only 2 divisors, it is 1 and the number itself."""

n = int(input())

if n < 2: 
    print("NO")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("YES")
    else:
        print("NO")