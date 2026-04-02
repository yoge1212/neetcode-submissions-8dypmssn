class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #[30,38,30,36,35,40,28]
        #[28, 40, 36, 38, 30]
        #[(30, 0)]

        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            current = (temperatures[i], i)
            while stack and stack[-1][0] <= current[0]:
                stack.pop()
            
            if stack:
                result[i] = stack[-1][1] - current[1]
            
            else:
                result[i] = 0

            stack.append(current)
           
        return result
