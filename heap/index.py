"""
    function to run singly linked list tests
"""

def run():
    import tests
    for i in dir(tests):
        item = getattr(tests, i)
        if callable(item) and str(i) != 'Heap':
            print str(i)
            item()

if __name__ == "__main__":
    run()
