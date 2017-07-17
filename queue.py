class Queue:

    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, item):
        self.enqueue_stack.append(item)

    def dequeue(self):
        while self.enqueue_stack:
            item = self.enqueue_stack.pop()
            self.dequeue_stack.append(item)
        return self.dequeue_stack.pop()


if __name__ == '__main__':
    queue = Queue()

    print(">>> queue.enqueue(1)")
    print(">>> queue.enqueue(2)")
    print(">>> queue.enqueue(5)")
    print(">>> queue.enqueue(7)")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(5)
    queue.enqueue(7)

    print("\n>>> queue.dequeue()")
    print(">>> queue.dequeue()")
    print(">>> queue.dequeue()")
    print(">>> queue.dequeue()")
    print( queue.dequeue() )
    print( queue.dequeue() )
    print( queue.dequeue() )
    print( queue.dequeue() )
