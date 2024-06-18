numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
count = 0
for i in numbers:
    for j in numbers:
        if i % j == 0:
            count += 1
    if count == 2:
        #print(i)
        primes.append(i)
    elif count != 2:
        not_primes.append(i)
    count = 0
print('Primes:',primes)
print('Not Primers:', not_primes)