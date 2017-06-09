array = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def binary_search(array, value):
    _min = 0
    _max = len(array) - 1

    while _max >= _min:
        middle = (_max + _min) // 2

        if array[middle] == value:
            return middle
        elif array[middle] > value:
            _max = middle - 1
        else:
            _min = middle + 1

    return -1

def binary_search_recursive(array, value, _min, _max):
    if _min > _max:
        return -1

    middle = (_max + _min) // 2

    if array[middle] == value:
        return middle

    elif array[middle] > value:
        return binary_search_recursive(array, value, _min, middle - 1)

    else:
        return binary_search_recursive(array, value, middle + 1, _max)

def testNotFound():
    assert binary_search(array, 99) == -1

def testFindStart():
    assert binary_search(array, 1) == 0

def testFindMiddle():
    assert binary_search(array, 13) == 5

def testFindEnd():
    assert binary_search(array, 89) == 9

def testNotFoundRecursive():
    assert binary_search_recursive(array, 99, 0, 9) == -1

def testFindStartRecursive():
    assert binary_search_recursive(array, 1, 0, 9) == 0

def testFindMiddleRecursive():
    assert binary_search_recursive(array, 13, 0, 9) == 5

def testFindEndRecursive():
    assert binary_search_recursive(array, 89, 0, 9) == 9

if __name__ == "__main__":
    testNotFound()
    testFindStart()
    testFindMiddle()
    testFindEnd()
    testNotFoundRecursive()
    testFindStartRecursive()
    testFindMiddleRecursive()
    testFindEndRecursive()
    