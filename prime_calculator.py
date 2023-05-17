def calculate_nth_prime(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes[-1]
