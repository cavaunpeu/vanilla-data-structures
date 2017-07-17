class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if value == self.value:
            return True
        if value < self.value:
            if self.left:
                return self.left.contains(value)
        else:
            if self.right:
                return self.right.contains(value)
        return False

    def printInOrder(self):
        if self.left:
            self.left.printInOrder()
        print(self.value)
        if self.right:
            self.right.printInOrder()


if __name__ == '__main__':
    print(f">>> node = Node(8)")
    print(f">>> node.insert(10)")
    print(f">>> node.insert(12)")
    print(f">>> node.insert(7)")
    print(f">>> node.insert(4)")
    print(f">>> node.insert(8)")
    print(f">>> node.insert(9)")
    print(f">>> node.insert(13)")

    node = Node(8)
    node.insert(10)
    node.insert(12)
    node.insert(7)
    node.insert(4)
    node.insert(8)
    node.insert(9)
    node.insert(13)

    print(f"\n>>> node.printInOrder()")
    node.printInOrder()

    print(f"\n>>> node.contains(7)")
    print(f">>> node.contains(13)")
    print(f">>> node.contains(5)")
    print(f">>> node.contains(6)")
    print(node.contains(7))
    print(node.contains(13))
    print(node.contains(5))
    print(node.contains(6))
