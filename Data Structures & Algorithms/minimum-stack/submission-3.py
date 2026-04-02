class MinStack:
    

    def __init__(self):
        self.stack = []
        self.current_min = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.current_min:
            self.current_min.append(val)

        elif val <= self.current_min[len(self.current_min) - 1]:
            self.current_min.append(val)

        

    def pop(self) -> None:
        new = self.stack.pop()
        if new == self.current_min[len(self.current_min) - 1]:
            self.current_min.pop()

        

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]
        

    def getMin(self) -> int:
    
        return self.current_min[len(self.current_min) - 1]

        
