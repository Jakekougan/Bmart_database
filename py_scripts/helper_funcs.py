import random


def upc_gen(n):
    '''Generates a given number of upc codes

    Parameters:
        n (int): amount of random upcs

    Returns:
        None '''

    while n > 0:
        codes = set()
        upc = ""
        for i in range(12):
            upc += str(random.randint(0,9))
        if upc not in codes:
            print("'"+upc+"'")
            n -=1

upc_gen(30)

