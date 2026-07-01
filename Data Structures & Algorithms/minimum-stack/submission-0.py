class MinStack:

    def __init__(self):
        self.Stack = []
        

    def push(self, val: int) -> None:
        self.Stack.append(val)
        print(self.Stack)
        return None

    def pop(self) -> None:
        self.Stack = self.Stack[:len(self.Stack) - 1] #remove Last List
        print(self.Stack)
        return None

    def top(self) -> int:
        return self.Stack[-1]
        

    def getMin(self) -> int:
        minNum = 2**31 
        print(minNum)
        # pop, top and getMin will always be called on non-empty stacks.
        #“How do I write −2 to the power of 31 in Python?”
        #** = exponentiation ^ = bitwise XOR ❌ (완전히 다름)
        if (len(self.Stack) == 0) :
            return 0

        for i in self.Stack : 
            if (i < minNum) : 
                minNum = i
        
        return minNum
            

