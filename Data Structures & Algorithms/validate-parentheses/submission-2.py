class Solution:
    def isValid(self, s: str) -> bool:
        #we are given a string s that consists of the charactesr:
        #'(', ')', '{', '}', '[', ']'

        #the input string s is valid if and only if
        #every open bracket is closed by the same type of brakcket
        #open brackets are closed in the correct order
        #every close bracket has. corresponding open bracket of the same type

        #wer need to return true if s is avalid string
        #otherwise return false

        #s = '[]'
        #s = '({[}])
        #stack = [. ({[ we come across a close bracket we try to pop fro mteh stack
        #since they dont match we return false otherwise keep going after popping
        #at the end return true if the stack is empty or not
       
        stack = []
        bracket_matches = {')': '(', '}': '{', ']': '['}
        for bracket in s:
            
            if bracket not in bracket_matches:
                print(bracket)
                stack.append(bracket)
            else:
                
                latest = stack.pop()
                if latest != bracket_matches[bracket]:
                    return False
        
        print(stack)
        if not stack:
            return True
        else:
            return False

        