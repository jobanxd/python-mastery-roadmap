# - **Day 6:** Create a function to check if a number is prime. Use arguments and return values.

def prime_checker(n: int) -> bool:
    if n <= 1:
        return True
    if n <= 3:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6

    return True


if __name__ == '__main__':
    n = int(input("Prime checker - Please input a integer: "))
    print(prime_checker(n))


# NEED TO LEARN THIS METHOD OF CHECKING PRIME!