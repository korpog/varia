class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def traverse(self):
        head = self.head
        while head is not None:
            print(head.value)
            head = head.next

    def push(self, value):
        new_node = Node(value)
        new_node.set_next(self.head)
        self.head = new_node

    def search(self, value):
        current = self.head
        exists = False
        while exists is False and current is not None:
            if current.get_value() == value:
                exists = True
            else:
                current = current.get_next()
            if current is None:
                raise ValueError('Value does not exist in the list')
        return current

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def delete(self, value):
        previous = None
        current = self.head
        exists = False
        while exists is False and current is not None:
            if current.get_value() == value:
                exists = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError('Value does not exist in the list')
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.push(5)
    linked_list.push(7)
    linked_list.push(9)
    linked_list.push(11)
    linked_list.delete(9)
    print()
    linked_list.traverse()
