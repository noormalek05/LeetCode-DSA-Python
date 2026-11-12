# Problem: 1342. Number of Steps to Reduce a Number to Zero
# Topic: Foundations / Mathematics
# Difficulty: Easy
# Approach: While Loop + If-Else


# ==========================================
# Solution 1: Using While Loop
# ==========================================

class Solution(object):
    def numberOfSteps(self, num):
        steps = 0

        while num > 0:
            if num % 2 == 0:
                num = num // 2
                steps += 1

            else:
                num = num - 1
                steps += 1

        return steps

# Time Complexity: O(log n)
# Space Complexity: O(1)
