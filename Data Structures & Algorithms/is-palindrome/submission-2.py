class Solution:
    def isPalindrome(self, s: str) -> bool:
        #we are given a string s and we need to return true if its a palindrome
        #otherwise we return false

        #a palindrom is a string that reads the same forward and backward it is also
        #case insensitive and ignores all non-alphanumeric characters
        

        #so we ignore anything that is not a alphanumeric character

        #"$..W$..as it a car or a cat I saw?"

        left = 0
        right = len(s) - 1

        while left < right:

            while left < len(s) - 1 and not self.isAlpha(s[left]):
                left += 1

            while right > -1 and not self.isAlpha(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True


    def isAlpha(self, c):
        return (ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z')) or (ord('0') <= ord(c) <= ord('9'))




        