number = int(input("Input number : "))

count = 0
#for i in range(1, number+1):
for i in range(2, number):  # -2 loop
    if number % i == 0:
        count = count + 1

#if count == 2:
if count == 0:
    print(f"{number} is prime number~")
else:
    print(f"{number} is NOT prime number!")

# Input number : 1
# 1 is prime number~
