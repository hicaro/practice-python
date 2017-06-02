from SinglyLinkedList import SinglyLinkedList


def testSizeEmpty():
    _list = SinglyLinkedList()
    assert _list.size() == 0


def testSize1to2():
    _list = SinglyLinkedList()
    _list.push_front(4)

    assert _list.size() == 1

    _list.push_front(9)
    assert _list.size() == 2


def testEmpty():
    _list = SinglyLinkedList()
    assert _list.is_empty()

    _list.push_front("word")
    assert not _list.is_empty()


def testValueAt():
    _list = SinglyLinkedList()
    _list.push_front(99)
    assert _list.value_at(0) == 99

    _list.push_front(3)
    _list.push_front(122)
    assert _list.value_at(0) == 122
    assert _list.value_at(1) == 3
    assert _list.value_at(2) == 99


def testPushFront():
    _list = SinglyLinkedList()
    _list.push_front(753)
    _list.push_front(159)

    assert _list.size() == 2
    assert _list.value_at(0) == 159
    assert _list.value_at(1) == 753


def testPopFront():
    _list = SinglyLinkedList()
    _list.push_front(12)
    _list.push_front(11)

    assert _list.pop_front() == 11
    assert _list.pop_front() == 12

def testPushBack():
    _list = SinglyLinkedList()
    _list.push_back(123)
    _list.push_back(456)

    assert _list.size() == 2
    assert _list.value_at(0) == 123
    assert _list.value_at(1) == 456


def testPopBack():
    _list = SinglyLinkedList()
    _list.push_back(33)
    _list.push_back(36)

    assert _list.pop_back() == 36
    assert _list.pop_back() == 33
    assert _list.size() == 0


def testInsertFromEmpty():
    _list = SinglyLinkedList()
    _list.insert(0, 3)
    assert _list.front() == 3


def testInsertFromNonEmpty():
    _list = SinglyLinkedList()
    _list.push_front(123)
    _list.insert(0, 3)
    assert _list.front() == 3
    assert _list.back() == 123


def testInsertBack():
    _list = SinglyLinkedList()
    _list.push_front(123)
    _list.insert(1, 3)

    assert _list.back() == 3


def testInsertMiddle():
    _list = SinglyLinkedList()
    _list.push_back(123)
    _list.push_back(456)
    _list.push_back(999)
    _list.insert(2, 777)

    assert _list.value_at(1) == 456
    assert _list.value_at(2) == 777
    assert _list.back() == 999


def testErase():
    _list = SinglyLinkedList()
    _list.push_back(44)
    _list.erase(0)

    assert _list.size() == 0


def testEraseFirst():
    _list = SinglyLinkedList()
    _list.push_back(44)
    _list.push_back(55)
    _list.erase(0)

    assert _list.size() == 1
    assert _list.front() == 55


def testEraseLast():
    _list = SinglyLinkedList()
    _list.push_back(44)
    _list.push_back(55)
    _list.erase(1)

    assert _list.size() == 1
    assert _list.front() == 44


def testValueNFromEnd():
    _list = SinglyLinkedList()
    _list.push_back(44)
    _list.push_back(55)
    _list.push_back(66)

    assert _list.value_n_from_end(1) == 66
    assert _list.value_n_from_end(2) == 55
    assert _list.value_n_from_end(3) == 44


def testReverseOne():
    _list = SinglyLinkedList()
    _list.push_back(44)

    _list.reverse()

    assert _list.front() == 44


def testReverseTwo():
    _list = SinglyLinkedList()
    _list.push_back(44)
    _list.push_back(55)

    _list.reverse()

    assert _list.front() == 55
    assert _list.back() == 44


def testReverseThree():
    _list = SinglyLinkedList()
    _list.push_back(44)
    _list.push_back(55)
    _list.push_back(66)

    _list.reverse()

    assert _list.value_at(0) == 66
    assert _list.value_at(1) == 55
    assert _list.value_at(2) == 44


def testRemoveNone():
    _list = SinglyLinkedList()
    _list.remove_value(5)

    assert _list.size() == 0


def testRemoveOnly():
    _list = SinglyLinkedList()
    _list.push_back(5)
    _list.remove_value(5)

    assert _list.size() == 0


def testRemoveFirst():
    _list = SinglyLinkedList()
    _list.push_back(5)
    _list.push_back(22)
    _list.remove_value(5)

    assert _list.size() == 1
    assert _list.front() == 22


def testRemoveLast():
    _list = SinglyLinkedList()
    _list.push_back(5)
    _list.push_back(22)
    _list.remove_value(5)

    assert _list.size() == 1
    assert _list.front() == 22


def testRemoveMiddle():
    _list = SinglyLinkedList()
    _list.push_back(5)
    _list.push_back(22)
    _list.remove_value(5)

    assert _list.size() == 1
    assert _list.front() == 22
