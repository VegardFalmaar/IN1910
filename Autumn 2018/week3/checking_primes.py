def is_prime(n):
    """This function takes in a positive integer n and returns True if n is a prime and False if n is not a prime."""
    assert isinstance(n, int) and n>0, 'Input must be a positive integer.'

    for i in range(2, n):
        if n%i == 0:
            return False

    return True