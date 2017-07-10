class MergeSort(object):
    '''
    __merge Sort sorting algorithm implementation
        - Best case: O(n log(n))
        - Average case: O(n log(n))
        - Worst case: O(n log(n))
    '''

    @staticmethod
    def __merge(array, aux, lo, mid, hi):

        for k in range(lo, hi + 1):
            aux[k] = array[k]

        i = lo
        j = mid + 1

        for k in range(lo, hi + 1):
            # all the first half was already copied
            if i > mid:
                array[k] = aux[j]
                j = j + 1
            # all the second half was already copied
            elif j > hi:
                array[k] = aux[i]
                i = i + 1
            # item from second half is smaller than item from first half one
            elif aux[j] < aux[i]:
                array[k] = aux[j]
                j = j + 1
            else:
                array[k] = aux[i]
                i = i + 1


    @staticmethod
    def __sort(array, aux, lo, hi):
        if lo >= hi:
            return

        mid = (lo + hi) // 2
        MergeSort.__sort(array, aux, lo, mid)
        MergeSort.__sort(array, aux, mid + 1, hi)

        if array[mid + 1] > array[mid]:
            return

        MergeSort.__merge(array, aux, lo, mid, hi)

    @staticmethod
    def sort(numbers=None):
        _len = len(numbers)
        aux = [0 for _ in range(_len)]
        MergeSort.__sort(numbers, aux, 0, _len -1)
