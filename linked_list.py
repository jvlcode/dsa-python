class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None

# Creating nodes
head = Node(10)
second = Node(20)
third = Node(30)

# Linking nodes
head.next = second
second.next = third

# Traversal
current = head
while current:
    print(current.data)
    current = current.next