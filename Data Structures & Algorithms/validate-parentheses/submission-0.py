class Solution:
    def isValid(self, s: str) -> bool:
        #we are given a string s with the following characters 
        #'(' ,')', '{', '}', '[', ']'
        #s is valid if and only if every open bracket is closed 
        #by the same type of close bracket
        #open brackets are closed in the correct order
        #every close bracket has a corresponding open bracket

        #we must return true if s is a valid string else return false
        #EX: s = "[]" output: true
        #EX: s = "([{}])" output: true
        #s = "[(])" output: false

        #we can use a stack. LIFO last in first out
        #we iterate through the string and only add open brackets
        #if we hit a close bracket we check to see the top of the stack. 
        #if the top of the stack is the corresponding open bracket we pop() it
        #we return false if it is not

        #Then we return True if the stack is empty

        #edge cases: only 1 input
        #only closing brackets: we need to see if stack isn't empty when checking

        stack = []
        brackets = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) < 1:
                    return False
                else:
                    if c == brackets[stack[-1]]:
                        stack.pop()
                    else:
                        return False
        return stack == []

        