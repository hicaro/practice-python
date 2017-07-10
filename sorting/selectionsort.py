class SelectionSort(object):
    '''
    Selection Sort sorting algorithm implementation
        - Best case: O(n^2)
        - Average case: O(n^2)
        - Worst case: O(n^2)
    '''

    @staticmethod
    def sort(numbers=None):
        _len = len(numbers)
        for i in range(_len - 1):
            _min = i

            for j in range(i+1, _len):
                if numbers[j] < numbers[_min]:
                    _min = j

            if _min != i:
                aux = numbers[i]
                numbers[i] = numbers[_min]
                numbers[_min] = aux
