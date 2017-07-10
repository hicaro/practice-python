
class BubbleSort(object):
    '''
    Bubble Sort sorting algorithm implementation
        - Best case: O(n)
        - Average case: O(n^2)
        - Worst case: O(n^2)
    '''
    @staticmethod
    def sort(numbers=None):
        _len = len(numbers)
        for i in range(_len - 1):
            for j in range(1, _len - i):
                if numbers[j-1] > numbers[j]:
                    aux = numbers[j]
                    numbers[j] = numbers[j-1]
                    numbers[j-1] = aux
