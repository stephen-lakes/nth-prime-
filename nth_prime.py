def nth_prime(n:int):
    primes:list = []
    counter:int = 2

    while len(primes) < n:

        if counter == 2 or counter == 3:
            primes.append(counter)
        else:
            for num in range(2, (counter // 2) + 1):
                if counter % num == 0:
                    break
            else:
                primes.append(counter)
        
        counter += 1

    return primes[-1]



# returns the 100001th prime number
print(nth_prime(100001))
