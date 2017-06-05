from queue import Queue


def testSizeEmpty():
    _queue = Queue()
    assert _queue.is_empty()

    _queue.enqueue(3)
    assert not _queue.is_empty()


def testSize1to2():
    _queue = Queue()
    _queue.enqueue(12.3)
    _queue.enqueue(4.235)
    _queue.enqueue(5.4)
    _queue.enqueue(7.0)
    _queue.enqueue(885314.32214)

    assert not _queue.is_empty()


def testEmpty():
    _queue = Queue()
    _queue.enqueue(100)
    _queue.enqueue(200)
    assert _queue.dequeue() == 100
    _queue.enqueue(300)
    assert _queue.dequeue() == 200
    _queue.enqueue(400)
    _queue.enqueue(500)
    _queue.enqueue(600)
    _queue.enqueue(700)
    assert _queue.dequeue() == 300
    assert _queue.dequeue() == 400
    assert _queue.dequeue() == 500
    assert _queue.dequeue() == 600
    assert _queue.dequeue() == 700

    assert _queue.is_empty()
