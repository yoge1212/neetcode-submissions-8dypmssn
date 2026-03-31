class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #keep track of count of letters if any count is greater than 3 or less than 1 its false
        if len(s) != len(t):
            return False
        
        mapS = {}
        mapT = {}
        for i in range(len(s)):
            if s[i] in mapS:
                mapS[s[i]] = mapS[s[i]] + 1
            else:
                mapS[s[i]] = 1

            if t[i] in mapT:
                mapT[t[i]] = mapT[t[i]] + 1
            else:
                mapT[t[i]] = 1

        for key in mapS:
            if key not in mapT:
                return False
                
            if mapS[key] != mapT[key] :
                return False
        return True

            