from bubblesort import BubbleSort
from insertionsort import InsertionSort
from selectionsort import SelectionSort
from mergesort import MergeSort
from quicksort import QuickSort

def isSorted(x, key = lambda x: x):
    return all([key(x[i]) <= key(x[i + 1]) for i in xrange(len(x) - 1)])

if __name__  == "__main__":
    to_sort = [613, 55, 8721, 472, 94, 72, 74, 8, 61, 356]
    _sorted = [8, 55, 61, 72, 74, 94, 356, 472, 613, 8721]

    #BubbleSort.sort(to_sort)
    #InsertionSort.sort(to_sort)
    #SelectionSort.sort(to_sort)
    #MergeSort.sort(to_sort)
    QuickSort.sort(to_sort)
    print to_sort
    assert isSorted(to_sort)
