start = int(input("Input start number : "))
end = int(input("Input end number : "))

for k in range(start, end+1):
    is_prime_number = True
    if k < 2:
        is_prime_number = False
    else:
        i = 2
        while i*i <= k:
            if k % i == 0:
                is_prime_number = False
                break
            i = i + 1
        if is_prime_number: print(k, end=' ')
