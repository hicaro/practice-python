"""
    function to run hash table list tests
"""

def run():
    import tests
    for i in dir(tests):
        item = getattr(tests, i)
        if callable(item):
            print str(i)
            item()

if __name__ == "__main__":
    run()
    