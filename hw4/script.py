nums = [3, 4, -1, 1]

nums.sort()

smallest_missing = 1

for num in nums:
    if num == smallest_missing:
        smallest_missing += 1

print(smallest_missing)
