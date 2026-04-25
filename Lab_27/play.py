def add(*args):
    sums = 0
    for n in args:
        sums += n
    return sums

total = add(5,10,15)
print(total)