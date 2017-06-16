""" Implementation of a binary search tree """

try:
    import Queue as Q # ver. < 3.0
except ImportError:
    import queue as Q

class BST(object):
    """ BST is a binary search tree implementation """

    class TreeNode(object):
        """ Single node to hold an element in a BST """
        def __init__(self, parent, value):
            self.parent = parent
            self.left = None
            self.right = None
            self.value = value


    def __init__(self):
        self.root = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        """ returns boolean true or false """
        return self._size == 0

    def insert(self, value):
        """ insert value into tree """
        if self.root is None:
            self.root = self.TreeNode(None, value)
        else:
            current = self.root
            while current.left and value < current.value or current.right and value > current.value:

                if value < current.value:
                    current = current.left

                elif value > current.value:
                    current = current.right

            if value < current.value:
                current.left = self.TreeNode(current, value)

            elif value > current.value:
                current.right = self.TreeNode(current, value)

            else:
                return

        self._size = self._size + 1

    def remove(self, value, node=None):
        """ remove a value from the tree """
        if node is None:
            node = self.root

        if node:
            current = node
            while current:

                if value < current.value:
                    current = current.left

                if value > current.value:
                    current = current.right

                if value == current.value:
                    break

            # value found
            if current:
                self._size = self._size - 1

                # has no children
                if current.left is None and current.right is None:
                    # node has a parent
                    if current.parent:
                        # is left
                        if current.parent.left == current:
                            current.parent.left = None
                        # is right
                        if current.parent.right == current:
                            current.parent.right = None

                    # it is the root
                    else:
                        self.root = None

                # contains only left child
                elif current.left and current.right is None:
                    # node has a parent
                    if current.parent:
                        # is left
                        if current.parent.left == current:
                            current.parent.left = current.left
                        # is right
                        if current.parent.right == current:
                            current.parent.right = current.left

                    # it is the root
                    else:
                        self.root = current.left

                # contains only right child
                elif current.left is None and current.right:
                    # node has a parent
                    if current.parent:
                        # is left
                        if current.parent.left == current:
                            current.parent.left = current.right
                        # is right
                        if current.parent.right == current:
                            current.parent.right = current.right

                    # it is the root
                    else:
                        self.root = current.right

                # has two children
                # copy the smallest element and delete it from the right subtree
                else:
                    _value = self.get_min(current.right)
                    current.value = _value
                    self.remove(_value, current.right)


    def get_node_count(self):
        """ get count of values stored """
        return self._size

    def pre_order(self):
        """ prints all tree values in tranversal pre order """
        return self.__pre_order(self.root)

    def __pre_order(self, node):
        """ recursively prints all tree values in tranversal pre order """
        if node:
            return [node.value] + self.__pre_order(node.left) + self.__pre_order(node.right)
        return []

    def in_order(self):
        """ prints all tree values in tranversal in order """
        return self.__in_order(self.root)

    def __in_order(self, node):
        """ recursively prints all tree values in tranversal in order """
        if node:
            return self.__in_order(node.left) + [node.value] + self.__in_order(node.right)
        return []

    def post_order(self):
        """ prints all tree values in tranversal post order """
        return self.__post_order(self.root)

    def __post_order(self, node):
        """ recursively prints all tree values in tranversal post order """
        if node:
            return self.__post_order(node.left) + self.__post_order(node.right) + [node.value]
        return[]

    def level_order(self):
        """ prints all tree values in tranversal level order """
        _print = []
        _queue = Q.Queue()
        _queue.put(self.root)

        while not _queue.empty():
            current = _queue.get()
            if current:
                _print.append(current.value)
                _queue.put(current.left)
                _queue.put(current.right)

        return _print

    def exists(self, value, node=None):
        """ checks whether a value exists in the tree """
        if node is None:
            node = self.root

        current = node

        while current:
            if current.value == value:
                return True
            elif current.value > value:
                current = current.left
            else:
                current = current.right

        if current is None:
            return False

    def get_height(self, node=None):
        """ returns the height in nodes (single node's height is 1) """
        if node is None:
            node = self.root

        return self.__get_height(node)

    def __get_height(self, node):
        """ recursively get the height of a tree """
        if node is None:
            return 0

        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def get_min(self, node=None):
        """ returns the minimum value stored in the tree """
        if node is None:
            node = self.root

        if node is None:
            return None

        current = node
        while current.left:
            current = current.left

        return current.value

    def get_max(self, node=None):
        """ returns the maximum value stored in the tree """
        if node is None:
            node = self.root

        if node is None:
            return None

        current = node
        while current.right:
            current = current.right

        return current.value

    def get_successor(self, value, node=None):
        """ returns next-highest value in tree after given value, None if none """
        if node is None:
            node = self.root

        # tree is empty
        if node is None:
            return None

        current = self.root
        while current:

            if value < current.value:
                current = current.left

            if value > current.value:
                current = current.right

            if value == current.value:
                break

        # value not found
        if current is None:
            return None

        # if there is a right subtree
        if current.right:
            return self.get_min(current.right)

        # return the first left ancestor
        _parent = current.parent
        while _parent and node == _parent.right:
            node = _parent
            _parent = _parent.parent

        if _parent:
            return _parent.value

        return None
