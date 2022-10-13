# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]


def twoSum(nums, target):
    output=[]
    for n in range(len(nums)):
        x = nums[n]
        y = target - nums[n]
        nums[n] = ""
        if nums.__contains__(y) == True:
            output = [n, nums.index(y)]
            return output


print(twoSum([5,3,4,2,95,50,45,158,-5,-4,0,27], 45))