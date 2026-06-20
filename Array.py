# Largest Element
arr = [2,2,5,6,6,7]

largest = arr[0]

for i in arr:
    if i > largest:
        largest = i

print(largest)


# Smallest Element
smallest = arr[0]

for i in arr:
    if i < smallest:
        smallest = i

print(smallest)


# Second Largest Element
arr = [10,20,30,40,50,60,70]

largest = float("-inf")
second_largest = float("-inf")

for i in arr:
    if i > largest:
        second_largest = largest
        largest = i

    elif i > second_largest and i != largest:
        second_largest = i

print(second_largest)


# Reverse Array
arr = [10,20,30,40,50,60,70]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]

    left += 1
    right -= 1

print(arr)


# Remove Duplicates
arr = [10,20,30,40,50,60,70]

left = 0

for right in range(1, len(arr)):
    if arr[right] != arr[left]:
        left += 1
        arr[left] = arr[right]

print(arr[:left+1])


# Move Zeroes
arr = [0,0,5,0,2]

left = 0

for right in range(len(arr)):
    if arr[right] != 0:
        arr[right], arr[left] = arr[left], arr[right]
        left += 1

print(arr)


# Missing Number
arr = [0,1,3]

for i in range(len(arr)+1):
    if i not in arr:
        print(i)
        break
