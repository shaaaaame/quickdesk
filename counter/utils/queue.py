class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item) -> None:
        # Using array methods:
        # self.queue.append(item)

        # Without array methods:
        self.queue = self.queue + [item]

    def dequeue(self):
        # Using array methods:
        # try:
        #   return self.queue.pop(0)
        # except:
        # raise IndexError("Queue is empty")
        
        # Without array methods:
        try:
            return_item = self.queue[0]
            self.queue = self.queue[1:]
            return return_item
        except:
            raise IndexError("Queue is empty")
        
        
    def getQueue(self) -> list[str]:
        return self.queue

    def size(self) -> int:
        return len(self.queue)
