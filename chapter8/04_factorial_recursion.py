from itertools import product


def fact(n):
    product=1
    for i in range(n):
        product=product*(i+1)
    return product

def fact2(n):
    if n==1 or n==0:
        return(1)
    else:
        f = n * fact2(n-1)
        return(f)

print(fact2(1))     