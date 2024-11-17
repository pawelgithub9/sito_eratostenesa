import math

def is_range_correct(n):
    if n > 2 and n%1==0:
        return True
    else:
        return False

    # short-hand(krótszy if): return True if n > 2 and n%1==0 else False

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)  # Tworzymy listę z wszystkimi wartościami True

    # 0 i 1 nie są liczbami pierwszymi
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    # Tworzymy listę z samymi liczbami pierwszymi z podanego przedziału
    prime_numbers = []

    for x in range(2, n+1):
        if is_prime[x] == True:
            prime_numbers.append(x)

    return prime_numbers

def print_sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)  # Tworzymy listę z wszystkimi wartościami True

    # 0 i 1 nie są liczbami pierwszymi
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    for x in range(2, n+1):
        if is_prime[x] == True:
            print(x)
            

if __name__ == '__main__':
    print("   ---   Sito Eratostenesa  ---   \n")

    n = int(input("Podaj n: "))

    if is_range_correct(n) == False:
        print("Podano nieprawidlowy przedzial!")
        quit()

    print(sieve_of_eratosthenes(n))
    print()
    print_sieve_of_eratosthenes(n)
