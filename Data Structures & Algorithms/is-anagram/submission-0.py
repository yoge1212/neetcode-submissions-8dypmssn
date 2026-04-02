class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #keep track of count of letters if any count is greater than 3 or less than 1 its false
        if len(s) != len(t):
            return False
        
        map = {}
        for i in range(len(s)):
            if s[i] in map:
                map[s[i]] = map[s[i]] + 1
            map[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in map:
                map[t[i]] = map[t[i]] + 1
            else:
                return False

        return True

            