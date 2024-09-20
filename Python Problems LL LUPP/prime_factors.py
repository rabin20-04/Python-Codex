def prime_factor(num):
    factors = []
    divisor = 2
    while num >= divisor:
        if num % divisor == 0:
            factors.append(divisor)
            num = num // divisor
        else:
            divisor += 1

    return factors


print("Prime factor of 20 are : ", prime_factor(20))
get_num = int(input("Enter any number : "))
print("Prime factors of the ", get_num, " are :", prime_factor(get_num))
print("Hello")
