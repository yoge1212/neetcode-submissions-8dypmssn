class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}

        stack = []

        for token in tokens:
            if token in operators:
                secondVal = stack.pop()
                firstVal = stack.pop()
                newVal = 0
                if token == '+':
                    newVal = firstVal + secondVal
                elif token == '-':
                    newVal = firstVal - secondVal
                elif token == '*':
                    newVal = firstVal * secondVal
                else:
                    newVal = int(firstVal / secondVal)
                stack.append(newVal)
            else:
                stack.append(int(token))
        return stack.pop(-1)
        