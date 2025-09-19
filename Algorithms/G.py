"""On the previous quiz, you needed to find n-th prime for Vanya. I think it was very easy, so let’s make it a little harder. You need to find a prime whose index is n-th prime. As an example prime numbers is: 2, 3, 5, 7... have indexes 1,2,3,4... so 2 and 3 indexes are primes too, therefore we have sequence of "superprimes" like: 3, 5, 11, 17... Find n-th superprime."""

#Just print n-th prime number.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    count = 0      
    num = 1         
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

 
N = int(input())
print(nth_prime(nth_prime(N)))