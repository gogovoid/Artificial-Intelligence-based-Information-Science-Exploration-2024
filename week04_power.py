def power(b, e) -> int:
    """
    Power function
    :param b: base number
    :param e: exponent number
    :return: power result value
    """
    result = 1
    for i in range(e):
        result = result * b
    return result


base, exponent = map(int, input("Input base & exponent number : ").split())
print(f"{base}^{exponent} = {base**exponent}")  # operator
print(f"{base}^{exponent} = {pow(base, exponent)}")  # built-in function
print(f"{base}^{exponent} = {power(base, exponent)}")  # custom function
