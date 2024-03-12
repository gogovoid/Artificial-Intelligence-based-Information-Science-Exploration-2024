number = int(input("Input number : "))

is_prime_number = True  # Change variable name from count to is_prime_number readably
if number < 2:
    is_prime_number = False
else:
    #for i in range(2, number):
    i = 2
    while i*i < number:  # reduce loop operation
        if number % i == 0:
            #is_prime_number = is_prime_number + 1
            is_prime_number = False  # Remove the plus operation
            break  # Exit the loop when the first divisor is found. Performance is improved when the input value is not a prime number.
        print(i, end=" ")
        i = i + 1

#if is_prime_number == 0:
if is_prime_number:  # Remove comparison (equivalent) operators
    print(f"{number} is prime number~")
else:
    print(f"{number} is NOT prime number!")
