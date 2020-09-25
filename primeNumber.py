def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True
    
def list_all_prime(maxLimit):
    for i in maxLimit:
        if isprime(i):
            print(i)

n = 5
if isprime(n):
    print(f'{n} is prime')
else:
    print(f'{n} not prime')
    


# OUTPUT
# 5 is prime
