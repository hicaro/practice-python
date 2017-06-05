"""
    Implementation of a singly linked list.
"""

class SinglyLinkedList(object):
    """ Singly linked list implementation using head and tail pointers """

    class Node(object):
        """ Single node to hold an element in a singly linked list """
        def __init__(self):
            self._value = None
            self._next = None

        def set_next(self, successor):
            """ sets next node pointer """
            self._next = successor

        def get_next(self):
            """ gets next node pointer """
            return self._next

        def set_value(self, value):
            """ sets value which node holds """
            self._value = value

        def get_value(self):
            """ gets value which node holds """
            return self._value


    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def size(self):
        """ returns number of data elements in list """
        return self._size

    def is_empty(self):
        """ bool returns true if empty """
        return self._size == 0

    def value_at(self, index):
        """ returns the value of the nth item (starting at 0 for first) """
        if self.is_empty():
            raise IndexError("List is empty")

        if index >= self._size:
            raise IndexError("Index out of bounds")

        current = self._head
        for _ in range(0, index):
            current = current.get_next()

        return current.get_value()

    def push_front(self, value):
        """ adds an item to the front of the list """
        node = self.Node()
        node.set_value(value)
        node.set_next(self._head)

        self._head = node
        if self._tail is None:
            self._tail = node

        self._size = self._size + 1

    def pop_front(self):
        """ remove front item and return its value """
        if self.is_empty():
            raise IndexError("List is empty")

        value = self._head.get_value()

        # contains only one element
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.get_next()

        self._size = self._size - 1
        return value


    def push_back(self, value):
        """ adds an item at the end """
        node = self.Node()
        node.set_value(value)

        # list is empty
        if self._head is None:
            self._head = node
        else:
            self._tail.set_next(node)

        self._tail = node
        self._size = self._size + 1


    def pop_back(self):
        """ removes end item and returns its value """
        if self.is_empty():
            raise IndexError("List is empty")

        value = self._tail.get_value()

        # contains only one element
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            previous = self._head
            while previous.get_next() != self._tail:
                previous = previous.get_next()

            previous.set_next(None)
            self._tail = previous

        self._size = self._size - 1
        return value

    def front(self):
        """ get value of front item """
        return self._head.get_value()

    def back(self):
        """ gets value of end item """
        return self._tail.get_value()

    def insert(self, index, value):
        """ inserts value at index,
        so current item at that index is pointed to by new item at index """
        if index == 0:
            self.push_front(value)
        elif index >= self._size:
            self.push_back(value)
        else:
            node = self.Node()
            node.set_value(value)

            current = self._head
            for _ in range(0, index - 1):
                current = current.get_next()

            node.set_next(current.get_next())
            current.set_next(node)

            self._size = self._size + 1

    def erase(self, index):
        """ removes node at given index """
        if self.is_empty():
            raise IndexError("List is empty")

        if index >= self._size:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.pop_front()
        elif index == self._size - 1:
            self.pop_back()
        else:
            current = self._head
            for _ in range(0, index - 1):
                current = current.get_next()


    def value_n_from_end(self, reverse_index):
        """ returns the value of the node at nth position from the end of the list """
        if self.is_empty():
            raise IndexError("List is empty")

        index = self._size - reverse_index
        if index < 0:
            raise IndexError("Index out of bounds")

        current = self._head
        for _ in range(0, index):
            current = current.get_next()

        return current.get_value()

    def reverse(self):
        """ reverses the list """
        if not self.is_empty():
            # contains two elements
            if self._head.get_next() == self._tail:
                aux = self._tail
                self._tail = self._head
                self._head = aux
            # contains three or more
            elif self._tail != self._head:
                current = self._head
                successor = self._head.get_next()

                while successor is not None:
                    aux = successor.get_next()
                    successor.set_next(current)

                    current = successor
                    successor = aux

                self._tail = self._head
                self._head = current
                self._tail.set_next(None)

    def remove_value(self, value):
        """ removes the first item in the list with this value """
        index = 0

        current = self._head
        while current is not None and current.get_value() != value:
            current = current.get_next()
            index = index + 1

        if current is not None:
            self.erase(index)
