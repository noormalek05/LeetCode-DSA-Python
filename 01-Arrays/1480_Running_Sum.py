# Problem: 1480. Running Sum of 1d Array
# Topic: Arrays
# Difficulty: Easy
# Approach: Prefix Sum (In-place)

class Solution(object):
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]

        return nums

# Time Complexity: O(n)
# Space Complexity: O(1)
