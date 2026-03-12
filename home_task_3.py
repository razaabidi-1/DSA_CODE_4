# Day 3
# Home Task 3: Sorting the Doubly Linked List
"""
Objective: Practice sorting algorithms on a doubly linked list.
Task: Write a method to sort the doubly linked list in ascending order.
Implement a simple sorting algorithm like bubble sort or selection sort that can handle node pointers.
Sort the list by rearranging the next and prev pointers instead of swapping data.
Example Output:
Input List: 40 -> 20 -> 30 -> 10 -> null
Sorted List: 10 -> 20 -> 30 -> 40 -> null
"""

# Program
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def display(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        result.append("null")
        return " -> ".join(result)

    def sort(self):
        if not self.head or not self.head.next:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    # Swap nodes by rearranging pointers
                    next_node = current.next
                    prev_node = current.prev
                    after_node = next_node.next

                    # Detach current and next_node
                    if prev_node:
                        prev_node.next = next_node
                    else:
                        self.head = next_node
                    next_node.prev = prev_node

                    next_node.next = current
                    current.prev = next_node

                    current.next = after_node
                    if after_node:
                        after_node.prev = current

                    swapped = True
                else:
                    current = current.next

# Output
if __name__ == "__main__":
    dll = DoublyLinkedList()
    for value in [40, 20, 30, 10]:
        dll.append(value)
    print("Input List:", dll.display())
    dll.sort()
    print("Sorted List:", dll.display())
