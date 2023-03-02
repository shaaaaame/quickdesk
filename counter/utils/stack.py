class Stack():
    def __init__(self):
        self.stack = []

    def push(self, item: str) -> None:
        # Using array methods: 
        # self.stack.append(item)

        # Without using array methods:
        self.stack = self.stack + [item]

    def pop(self) -> str:
        # Using array methods: 
        # return self.stack.pop()

        # Without using array methods:
        self.stack = self.stack[:-1]
        
    def getStack(self) -> list[str]:
        return self.stack

    def size(self) -> int:
        return len(self.stack)