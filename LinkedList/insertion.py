class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

head, tail = None, None

head = LinkedList(10)
tail = head
node1 = LinkedList(20)
head.next = node1
tail = node1


node2 = LinkedList(30)
node1.next = node2
tail = node2

node3 = LinkedList(40)
node2.next = node3
tail = node3

print(head.value)
print(head.next.value)
print(head.next.next.value)
print(head.next.next.next.value)
print(tail.value)