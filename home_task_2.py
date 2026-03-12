# Day 2
# Home Task 2: Finding and Counting Elements
"""
Objective: Develop skills to find nodes and count occurrences.
Task: Write two methods:
- A find method that searches for a value and returns its position or -1 if not found.
- A countOccurrences method that counts how many times a specified value appears in the list.
Example Output:
Input List: 10 -> 20 -> 30 -> 20 -> 40 -> null
Find Position of 30: Position 2
Count Occurrences of 20: 2
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

    def find(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def countOccurrences(self, value):
        count = 0
        current = self.head
        while current:
            if current.data == value:
                count += 1
            current = current.next
        return count

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
    for value in [10, 20, 30, 20, 40]:
        dll.append(value)
    print("Input List:", dll.display())
    pos = dll.find(30)
    print("Find Position of 30:", f"Position {pos}" if pos != -1 else "Not found")
    count = dll.countOccurrences(20)
    print("Count Occurrences of 20:", count)
