"""
Christopher Ijams
Doubly Linked List
Linear data structure of non-contiguous memory location with
pointers to the next and previous nodes.
"""


class PyDoublyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        curr = self.head
        definition = ""
        while curr:
            definition += str(curr.data) + ", "
            curr = curr.next
        return definition[:-2]

    # Adds a value to the linked list.
    def add(self, data):
        if not self.head:
            self.head = self._Node(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = self._Node(data)
            curr.next.prev = curr

    # Returns the reverse order of the list.
    def reverse_list(self):
        curr = self.head
        r_list = ""
        while curr.next:
            curr = curr.next
        while curr:
            r_list += str(curr.data) + ", "
            curr = curr.prev
        return r_list[:-2]

    # Returns the size of the linked list.
    def size(self):
        curr = self.head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        return size

    # Returns True if the list contains a value.
    def contains(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    # Returns the node containing the specified data.
    def get(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return curr
            curr = curr.next
        return False

    # Returns the first element in the list.
    def get_first(self):
        return self.head

    # Returns the last element in the list.
    def get_last(self):
        curr = self.head
        if curr:
            while curr.next:
                curr = curr.next
            return curr.data
        return curr

    # Removes first encountered specified element from the list.
    def remove(self, data):
        curr = self.head
        if self.size() == 1:
            self.head = None
        else:
            while curr:
                if curr.data == data:
                    if curr.prev:
                        curr.prev.next = curr.next
                    if curr.next:
                        curr.next.prev = curr.prev
                curr = curr.next

    # Returns the approximate middle of the list.
    def middle(self):
        if self.head:
            slow = fast = self.head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow.data

    # Clears the linked list.
    def clear(self):
        self.head = None

    # Reverses the linked list.
    def reverse(self):
        curr = self.head
        temp = None
        if curr:
            while curr:
                temp = curr.prev
                curr.prev = curr.next
                curr.next = temp
                curr = curr.prev
            self.head = temp.prev

    # Deletes the middle node of the list.
    def delete_middle_node(self):
        slow = fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if slow.prev:
            slow.prev.next = slow.next
            slow.next.prev = slow.prev

    # Returns the kth to last element in the list.
    def return_kth_to_last_element(self, k):
        length = 0
        curr = self.head
        while curr:
            curr = curr.next
            length += 1
        curr = self.head
        index = 0
        length = length-k
        try:
            while index != length:
                curr = curr.next
                index += 1
        except AttributeError as e:
            return e
        return curr.data

    # Removes any duplicates from the list.
    def remove_duplicates(self):
        hs = set()
        curr = self.head
        while curr:
            if curr.data in hs:
                self.remove(curr.data)
            else:
                hs.add(curr.data)
            curr = curr.next

    # Returns True if the linked list is a palindrome.
    def is_palindrome(self):
        start = end = self.head
        while end.next:
            end = end.next

        while start:
            if start.data != end.data:
                return False
            start = start.next
            end = end.prev
        return True

    # Node class for data storage with pointers for next and previous values.
    class _Node:
        def __init__(self, data=None, next_node=None, prev_node=None):
            self.data = data
            self.next = next_node
            self.prev = prev_node


class NotInListError(Exception):
    print("This value is not in the list")
