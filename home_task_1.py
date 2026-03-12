# Day 1
# Home Task 1: Inserting at a Specific Position
"""
Objective: Practice inserting nodes at a specific position in the list.
Task: Write a method in the DoublyLinkedList class to insert a node at a given position (0-based index).
If the position is 0, insert at the beginning. Otherwise, traverse the list to insert the node at the specified index.
Example Output:
Input List: 10 -> 20 -> 40 -> null
Insert 30 at position 2: 10 -> 20 -> 30 -> 40 -> null
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

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return
        current = self.head
        index = 0
        while current and index < position - 1:
            current = current.next
            index += 1
        if not current:
            raise IndexError("Position out of bounds")
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def display(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        result.append("null")
        return " -> ".join(result)

# Output
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_position(10, 0)
    dll.insert_at_position(20, 1)
    dll.insert_at_position(40, 2)
    print("Input List:", dll.display())
    dll.insert_at_position(30, 2)
    print("After inserting 30 at position 2:", dll.display())
