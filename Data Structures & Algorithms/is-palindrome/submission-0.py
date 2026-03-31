class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()


        for i in range(len(newStr)):
            if newStr[i] != newStr[len(newStr) - 1 - i]:
                return False
        
        return True



        