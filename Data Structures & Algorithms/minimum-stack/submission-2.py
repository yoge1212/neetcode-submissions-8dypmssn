class MinStack:
    

    def __init__(self):
        self.stack = []
        self.current_min = []
        self.popped = set()
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.current_min:
            self.current_min.append(val)

        elif val <= self.current_min[len(self.current_min) - 1]:
            self.current_min.append(val)

        

    def pop(self) -> None:
        new = self.stack.pop()
        self.popped.add(new)

        

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]
        

    def getMin(self) -> int:
    
        while self.current_min[len(self.current_min) - 1] in self.popped:
            self.current_min.pop()
        
        return self.current_min[len(self.current_min) - 1]

        
