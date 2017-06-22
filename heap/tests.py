from heap import Heap

def test_is_empty():
    _heap = Heap(10)

    assert _heap.is_empty()
    assert _heap.get_size() == 0

def test_insert():
    _heap = Heap(10)

    _heap.insert(23, "hello")
    assert not _heap.is_empty()
    assert _heap.get_size() == 1

    _heap.insert(9827, "world")
    assert _heap.get_size() == 2

    _heap.insert(662, "C++")
    _heap.insert(551, "nice")
    _heap.insert(1221, "things")
    assert _heap.get_size() == 5

def test_get_max():
    _heap = Heap(10)

    _heap.insert(23, "hello")
    _heap.insert(9827, "world")
    _heap.insert(662, "C++")
    _heap.insert(551, "nice")
    _heap.insert(1221, "things")

    _max = _heap.get_max()

    assert _max.key == 9827
    assert _max.value == "world"

def test_extract_max():
    _heap = Heap(10)

    _heap.insert(23, "hello")
    _heap.insert(9827, "world")
    _heap.insert(662, "C++")
    _heap.insert(551, "nice")
    _heap.insert(1221, "things")

    _max = _heap.extract_max()

    assert _max.key == 9827
    assert _max.value == "world"
    assert _heap.get_size() == 4

    _max = _heap.extract_max()

    assert _max.key == 1221
    assert _max.value == "things"
    assert _heap.get_size() == 3

def test_remove():
    _heap = Heap(10)

    _heap.insert(23, "hello")
    _heap.insert(662, "C++")
    _heap.insert(551, "nice")

    _heap.remove(2)
    assert _heap.get_size() == 2
    _heap.remove(0)
    _heap.remove(0)
    assert _heap.get_size() == 0

def test_heapsort():
    to_sort = [613, 55, 8721, 472, 94, 72, 74, 8, 61, 356]
    print to_sort

    #Heap.heapify(to_sort)
    #print to_sort

    Heap.heapsort(to_sort)
    print to_sort
