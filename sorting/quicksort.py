class QuickSort(object):
    '''
    Quick Sort sorting algorithm implementation
        - Best case: O(n log(n))
        - Average case: O(n log(n))
        - Worst case: O(n ^ 2)
    '''

    @staticmethod
    def sort(numbers=None):
        QuickSort.__sort(numbers, 0, len(numbers) - 1)

    @staticmethod
    def __partition(array, lo, hi):
        pivot = array[(lo + hi) // 2]
        indexLo = lo
        indexHi = hi

        while indexLo < indexHi:
            # find its location coming from the bottom
            while array[indexLo] < pivot:
                if indexLo == hi:
                    break
                indexLo += 1

            # find its location coming from the top
            while array[indexHi] > pivot:
                if indexHi == lo:
                    break
                indexHi -= 1

            # exchange places
            aux = array[indexLo]
            array[indexLo] = array[indexHi]
            array[indexHi] = aux

        return indexLo

    @staticmethod
    def __sort(array, lo, hi):
        if lo >= hi:
            return

        j = QuickSort.__partition(array, lo, hi)
        QuickSort.__sort(array, lo, j - 1)
        QuickSort.__sort(array, j + 1, hi)
