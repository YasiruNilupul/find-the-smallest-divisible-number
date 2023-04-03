primes = [2, 3, 5, 7, 11, 13, 17, 19]
num = 1
for prime in primes:
    num *= prime

while True:
    for i in range(1, 21):
        if num % i != 0:
            break
    else:
        print(num)
        break

    num += primes[-1]  # Increment by the product of primes
