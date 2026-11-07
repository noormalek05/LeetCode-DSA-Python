# Problem: 1672. Richest Customer Wealth
# Topic: Arrays (2D Array / Matrix)
# Difficulty: Easy
# Approach: Nested Loops

class Solution(object):
    def maximumWealth(self, accounts):
        wealth = 0

        for i in accounts:
            total = 0

            for j in i:
                total = total + j

            if total > wealth:
                wealth = total

        return wealth

# Time Complexity: O(m * n)
# Space Complexity: O(1)
