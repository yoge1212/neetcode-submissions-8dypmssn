class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        left = 0
        right = 0
        maxLen = 1

        while right < len(s):
            counter[s[right]] = counter.get(s[right], 0) + 1
            length = right - left + 1
            if length - max(counter.values()) <= k:
                maxLen = max(length, maxLen)
            else:
                counter[s[left]] = counter.get(s[left]) - 1
                left+=1
            right +=1
        
        return maxLen
        