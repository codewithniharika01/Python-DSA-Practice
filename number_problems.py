# Sum of Digits
n = 4567
total = 0

while n > 0:
    digit = n % 10
    total += digit
    n = n // 10

print(total)


# Reverse Number
n = 1234
num = n
result = 0

while num > 0:
    digit = num % 10
    result = result * 10 + digit
    num = num // 10

print(result)


# Palindrome Number
n = 1221
num = n
result = 0

while num > 0:
    digit = num % 10
    result = result * 10 + digit
    num = num // 10

if result == n:
    print("Palindrome")
else:
    print("Not Palindrome")


# Count Even Digits
n = 48296
count = 0
num = n

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        count += 1

    num = num // 10

print(count)


# Count Odd Digits
n = 4829671
count = 0
num = n

while num > 0:
    digit = num % 10

    if digit % 2 != 0:
        count += 1

    num = num // 10

print(count)


# Largest Digit
n = 48296
num = n
largest = 0

while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    num = num // 10

print(largest)


# Smallest Digit
n = 48296
num = n
smallest = 9

while num > 0:
    digit = num % 10

    if digit < smallest:
        smallest = digit

    num = num // 10

print(smallest)


# Product of Digits
n = 234
num = n
product = 1

while num > 0:
    digit = num % 10
    product *= digit
    num = num // 10

print(product)


# Count Digits Greater Than 5
n = 4829671
num = n
count = 0

while num > 0:
    digit = num % 10

    if digit > 5:
        count += 1

    num = num // 10

print(count)


# Largest Odd Digit
n = 4829671
num = n
largest = 0

while num > 0:
    digit = num % 10

    if digit % 2 != 0 and digit > largest:
        largest = digit

    num = num // 10

print(largest)


# Smallest Odd Digit
n = 4829671
num = n
smallest = 9

while num > 0:
    digit = num % 10

    if digit % 2 != 0 and digit < smallest:
        smallest = digit

    num = num // 10

print(smallest)


# Sum of Odd Digits
n = 4829671
num = n
total = 0

while num > 0:
    digit = num % 10

    if digit % 2 != 0:
        total += digit

    num = num // 10

print(total)


# Count Zeroes
n = 10020030
num = n
count = 0

while num > 0:
    digit = num % 10

    if digit == 0:
        count += 1

    num = num // 10

print(count)
