class InsertionSort(object):
    '''
    Insertion Sort sorting algorithm implementation
        - Best case: O(n)
        - Average case: O(n^2)
        - Worst case: O(n^2)
    '''

    @staticmethod
    def sort(numbers=None):
        _len = len(numbers)
        for i in range(1, _len):
            to_insert = numbers[i]
            j = i-1

            while j >= 0 and numbers[j] > to_insert:
                numbers[j+1] = numbers[j]
                j=j-1

            numbers[j+1] = to_insert
