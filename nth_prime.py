def is_prime(n:int) -> bool:
    """
    check if a number is prime.
    """
    if n == 0 or n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for num in range(2, (n//2) + 1):
            if n % num == 0:
                return False
        else:
            return True


def nth_prime(n:int) -> int:
    """
    returns the nth prime.
    """
    prime:int = 0
    count:int = 0

    while count < n:
        prime = prime + 1
        if is_prime(prime):
            count = count + 1

    return prime


# prints the 100001th prime number
print(nth_prime(10001)) 
