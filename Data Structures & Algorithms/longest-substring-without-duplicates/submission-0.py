class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        l = 0

        maxLen = 0
        tracker = set()


        for r in range(len(s)):
            while s[r] in tracker:
                tracker.remove(s[l])
                l += 1
            
            tracker.add(s[r])
            maxLen = max(maxLen, r - l + 1)

        return maxLen
        