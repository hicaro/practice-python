"""
    Implementation of a hash table.
"""

class HashTable(object):
    """ Hash table implementation using universal hashing with linear probing """

    class HashObject(object):
        """ Single hash element """
        def __init__(self):
            self.value = None
            self.key = None

    def __init__(self, size=0):
        self.size = size
        self.table = [None for _ in range(0, self.size)]

    def __hash(self, key, trial):
        return (self.__auxiliary_hash(key) + trial) % self.size

    def __auxiliary_hash(self, key):
        _hash = 0
        _length = len(key)

        for i in range(0, _length):
            _hash = _hash * 31 + ord(key[i])

        return (int)(_hash % self.size)

    def add(self, key, value):
        """ if key already exists, update value """
        trial = 0

        while trial < self.size:
            index = self.__hash(key, trial)

            if self.table[index] is None:
                self.table[index] = self.HashObject()
                self.table[index].key = key
                self.table[index].value = value
                break

            elif self.table[index].key is None or self.table[index].key == key:
                self.table[index].key = key
                self.table[index].value = value
                break

            trial = trial + 1

    def remove(self, key):
        """ remove a given key from the table """
        trial = 0

        while trial < self.size:
            index = self.__hash(key, trial)

            if self.table[index] is None:
                break

            elif self.table[index].key == key:
                self.table[index].key = None
                self.table[index].value = None

            trial = trial + 1

    def get(self, key):
        """ get value associated with a given key from the table """
        trial = 0

        while trial < self.size:
            index = self.__hash(key, trial)

            if self.table[index] is None:
                break

            elif self.table[index].key == key:
                return self.table[index].value

            trial = trial + 1

        return None

    def exists(self, key):
        """ checks whether a certain key exists in the table """
        trial = 0

        while trial < self.size:
            index = self.__hash(key, trial)

            if self.table[index] is None:
                return False

            elif self.table[index].key == key:
                return True

            trial = trial + 1

        return False
