# Valid Anagram

# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
#
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#
# Example 1:
#
# Input: s = "racecar", t = "carrace"
#
# Output: true
# Example 2:
#
# Input: s = "jar", t = "jam"
#
# Output: false
# Constraints:
#
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash, t_hash = {}, {}

        for i in range(len(s)):
            s_hash[s[i]] = s_hash.get(s[i], 0) + 1
            t_hash[t[i]] = t_hash.get(t[i], 0) + 1

        return s_hash == t_hash


if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("racecar", "carrace"))  # True
    print(solution.isAnagram("jar", "jam"))  # False
