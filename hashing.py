# Two Sum
arr = [2,7,11,15]
target = 9

seen = {}

for i in range(len(arr)):
    need = target - arr[i]

    if need in seen:
        print(seen[need], i)

    seen[arr[i]] = i


# Duplicate Number
arr = [1,3,4,2,2]

seen = set()

for i in arr:
    if i in seen:
        print(i)
        break

    seen.add(i)


# Duplicate Number
arr = [5,1,4,3,1]

seen = set()

for i in arr:
    if i in seen:
        print(i)
        break

    seen.add(i)
