from typing import List


# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# Example 1:
#
# Input: nums = [1, 2, 3, 3]
#
# Output: true
#
# Example 2:
#
# Input: nums = [1, 2, 3, 4]
#
# Output: false


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = set(nums)
        return len(hs) < len(nums)


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.hasDuplicate([1, 2, 3, 1]))  # Output: True
    print(solution.hasDuplicate([1, 2, 3, 4]))  # Output: False
    print(solution.hasDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Output: True
