number = int(input("Input number : "))

if number < 2:
    count = 1
else:
    count = 0
    for i in range(2, number):  # -2 loop
        if number % i == 0:
            count = count + 1

if count == 0:
    print(f"{number} is prime number~")
else:
    print(f"{number} is NOT prime number!")
