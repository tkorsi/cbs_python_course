def square_list(nums: list) -> list:
    position = len(nums) - 1
    ret = [0]*len(nums)
    left, right = 0, len(nums) - 1
    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2
        if left_square > right_square:
            ret[position] = left_square
            left += 1
        else:
            ret[position] = right_square
            right -= 1
        position -= 1
    return ret


assert square_list([-5, -1, 1, 2, 3]) == [1, 1, 4, 9, 25]
assert square_list([1, 2, 3]) == [1, 4, 9]
assert square_list([]) == []
assert square_list([5, 5, 5, 5]) == [25, 25, 25, 25]
assert square_list([-10]) == [100]
assert square_list([0, 2, 3]) == [0, 4, 9]
assert square_list([-1000, -500, 500, 1000]) == [250000, 250000, 1000000, 1000000]
print("All test cases pass.")
