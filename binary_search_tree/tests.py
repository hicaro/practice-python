from BinarySearchTree import BST

def testIsEmpty():
    _tree = BST()
    assert _tree.is_empty()

def testOneInsert():
    _tree = BST()
    _tree.insert(30)

    assert _tree.exists(30)

def testManyInsert():
    _tree = BST()
    _tree.insert(25)
    _tree.insert(10)
    _tree.insert(30)
    _tree.insert(35)

    assert _tree.exists(10)
    assert _tree.exists(25)
    assert _tree.exists(30)
    assert _tree.exists(35)

def testGetMin():
    _tree = __create_tree()

    assert _tree.get_min() == 1

def testGetMax():
    _tree = __create_tree()

    assert _tree.get_max() == 17

def testGetHieght():
    _tree = __create_tree()

    assert _tree.get_height() == 4

def testRemoveRootOne():
    _tree = BST()
    _tree.insert(7)
    _tree.remove(7)

    assert _tree.is_empty()

def testRemoveRootMany():
    _tree = __create_tree()
    _tree.remove(7)

    assert _tree.root.value == 8

def testRemoveLeaves():
    _tree = __create_tree()
    _tree.remove(1)
    _tree.remove(17)

    assert _tree.get_min() == 3
    assert _tree.get_max() == 15

def testIsBinarySearchTree():
    _tree = __create_tree()

    assert _tree.is_binary_search_tree_in_order()

def testIsNotBinarySearchTree():
    _tree = __create_tree()
    _tree.root.value = 2

    assert not _tree.is_binary_search_tree_in_order()

def __create_tree():
    _tree = BST()
    _tree.insert(7)
    _tree.insert(5)
    _tree.insert(3)
    _tree.insert(1)
    _tree.insert(4)
    _tree.insert(6)
    _tree.insert(12)
    _tree.insert(9)
    _tree.insert(8)
    _tree.insert(10)
    _tree.insert(15)
    _tree.insert(13)
    _tree.insert(17)

    return _tree
