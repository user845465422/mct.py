from random import randint
from time import time


num = int(input("Enter the number of digits of multipliers: "))
while 1:
    a = randint(10**(num - 1), 10**num - 1)
    b = randint(10**(num - 1), 10**num - 1)
    string = "Solve this - " + str(a) + "*" + str(b) + ": "
    sec = time()
    c = int(input(string))
    while a*b != c:
        c = int(input("Wrong. Try again: "))
    print("It took you {:.5} seconds.".format(time() - sec))
