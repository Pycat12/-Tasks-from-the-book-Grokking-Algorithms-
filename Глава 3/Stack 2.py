def fact(x):
    fact(3)
    if x == 1:
        return 1
    else:
        return x * fact(x-1)