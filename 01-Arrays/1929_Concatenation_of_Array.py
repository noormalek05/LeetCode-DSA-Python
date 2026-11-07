# Problem: 1929. Concatenation of Array
# Topic: Arrays
# Difficulty: Easy


# ==========================================
# Solution 1: Pre-allocation (Using Indexing)
# ==========================================

class Solution(object):
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0] * (2 * n)

        for i in range(0, n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]

        return ans

# Time Complexity: O(n)
# Space Complexity: O(n)


# ==========================================
# Solution 2: Two Traversals (Using append)
# ==========================================

class Solution(object):
    def getConcatenation(self, nums):
        ans = []

        for i in range(len(nums)):
            ans.append(nums[i])

        for i in range(len(nums)):
            ans.append(nums[i])

        return ans

# Time Complexity: O(n)
# Space Complexity: O(n)
