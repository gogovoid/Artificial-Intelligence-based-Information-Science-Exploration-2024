number = int(input("Input number : "))

count = 0
for i in range(1, number+1):
    if number % i == 0:
        count = count + 1

if count == 2:
    print(f"{number} is prime number~")
else:
    print(f"{number} is NOT prime number!")
