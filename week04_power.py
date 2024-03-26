base, exponent = map(int, input("Input base & exponent number : ").split())
print(f"{base}^{exponent} = {base**exponent}")  # operator
print(f"{base}^{exponent} = {pow(base, exponent)}")  # built-in function
