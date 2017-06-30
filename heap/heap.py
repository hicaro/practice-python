""" Implementation of heap and heapfy using implicit method """

class Heap(object):
    """ Heap class """

    class Item(object):
        """ Heap item """

        def __init__(self):
            self.key = None
            self.value = None

    def __init__(self, size):
        self._size = 0
        self._capacity = size
        self._array = [self.Item() for _ in range(0, self._capacity)]

    def __len__(self):
        return self._size

    def get_size(self):
        """ returns number of stored elements """
        return self._size

    def is_empty(self):
        """ returns boolean true or false """
        return self._size == 0

    def __parent(self, index):
        """ retrieves parent index of a given node """
        return (index - 1) // 2

    def __left_child(self, index):
        """ retrieves left child index of a given node """
        return 2 * index + 1

    def __right_child(self, index):
        """ retrieves right child index of a given node """
        return 2 * index + 2

    def __sift_up(self, index):
        """ bumps an element up to it right place """
        while index > 0:
            parent = self.__parent(index)

            if self._array[parent].key < self._array[index].key:

                aux = self._array[parent]
                self._array[parent] = self._array[index]
                self._array[index] = aux

                index = parent

            else:
                break

    def __sift_down(self, index):
        """ bumps an element down to it right place """
        swap_index = index

        left = self.__left_child(index)
        if left < self._size and self._array[left].key > self._array[swap_index].key:
            swap_index = left

        right = self.__right_child(index)
        if right < self._size and self._array[right].key > self._array[swap_index].key:
            swap_index = right

        if swap_index != index:
            aux = self._array[swap_index]
            self._array[swap_index] = self._array[index]
            self._array[index] = aux

            self.__sift_down(swap_index)

    def insert(self, key, value):
        """ insert a new item in the heap """
        assert self._size < self._capacity

        self._array[self._size].key = key
        self._array[self._size].value = value

        self.__sift_up(self._size)

        self._size = self._size + 1

    def get_max(self):
        """ returns the max item, without removing it """
        assert self._size > 0

        return self._array[0]

    def extract_max(self):
        """  returns the max item, removing it """
        assert self._size > 0

        _max = self._array[0]
        self._array[0] = self._array[self._size - 1]
        self._array[self._size - 1] = _max

        self._size = self._size - 1

        self.__sift_down(0)
        return _max

    def remove(self, index):
        """ removes item at index x """
        assert index >= 0 and index < self._size

        aux = self._array[index]
        self._array[index] = self._array[self._size - 1]
        self._array[self._size] = aux

        self._size = self._size - 1

        self.__sift_down(index)

    @staticmethod
    def heapify(numbers=None):
        """ creates a heap from the given array """
        _count = len(numbers)
        for index in reversed(range(_count // 2)):
            Heap.percolate_down(numbers, _count, index)

    @staticmethod
    def heapsort(numbers=None):
        """ heapsort method """
        Heap.heapify(numbers)
        _count = len(numbers)
        for index in reversed(range(1, _count)):
            aux = numbers[index]
            numbers[index] = numbers[0]
            numbers[0] = aux

            Heap.percolate_down(numbers, index, 0)

    @staticmethod
    def percolate_down(numbers=None, count=0, index=0):
        """ bumps an element down to it right place """
        swap_index = index

        left = 2 * index + 1
        if left < count and numbers[left] > numbers[swap_index]:
            swap_index = left

        right = 2 * index  + 2
        if right < count and numbers[right] > numbers[swap_index]:
            swap_index = right

        if swap_index != index:
            aux = numbers[swap_index]
            numbers[swap_index] = numbers[index]
            numbers[index] = aux

            Heap.percolate_down(numbers, count, swap_index)
