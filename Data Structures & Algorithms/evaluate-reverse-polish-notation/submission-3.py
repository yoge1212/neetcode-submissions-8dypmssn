class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        symbols = {'+', '-', '*', '/'}

        for token in tokens:
           
            if token not in symbols:
                stack.append(token)
                print(token)
                print(stack)
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                if token == "+":
                    result = first + second
                elif token == "-":
                    result = first - second
                elif token == "*":
                    result = first * second
                else:
                    result = first / second
                stack.append(result)

        return int(stack[-1])

        