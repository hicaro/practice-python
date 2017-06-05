"""
    A linked list based queue implementation
"""

from SinglyLinkedList import SinglyLinkedList

class Queue(object):
    """ Queue class """

    def __init__(self):
        self._list = SinglyLinkedList()

    def is_empty(self):
        """ bool returns true if empty """
        return self._list.is_empty()

    def enqueue(self, value):
        """ adds value at position at tail """
        self._list.push_back(value)

    def dequeue(self):
        """ returns value and removes least recently added element (front) """
        return self._list.pop_front()
