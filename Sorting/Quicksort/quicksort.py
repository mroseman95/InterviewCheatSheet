import time, random

def quicksort(A, l=None, r=None):
    """
    quicksort takes a list A and performs the quicksort algorithm on a sublist, and returns the resulting sublist sorted.
    @param A: A list of elements that can be compared to each other
    @param l: The leftmost index of the sublist
    @param r: The rightmost index of the sublist
    @return: A list that contains the same elements of A but in sorted order
    """
    if l is None:
        l = 0
    if r is None:
        r = len(A) - 1 if len(A) > 0 else 0

    if r <= l:
        return A

    p = partition(A, l, r)

    quicksort(A, l, p-1)
    quicksort(A, p+1, r)

    return A


def partition(A, l, r):
    """
    partition takes a list A and partitions a sublist around some pivot
    @param A: A list of elements that can be compared to each other
    @param l: The leftmost index of the sublist
    @param r: The rightmost index of the sublist
    @return: The index of the partition number
    """
    p = set_pivot(A, l, r)
    i = l
    for j in xrange(l, r):
        if A[j] <= p:
            # swap index i and j
            A[i], A[j] = A[j], A[i]
            i += 1

    # swap index i+1 and r
    A[i], A[r] = A[r], A[i]

    return i

def set_pivot(A, l, r):
    """
    set_pivot takes a list A and determines where the pivot should be for a quicksort algorithm on a sublist of A. It
    then swaps this pivot element with A[r]
    @param A: An array of elements that can be compared to each other
    @param l: The leftmost index of the sublist
    @param r: The rightmost index of the sublist
    @return: The value of the pivot
    """
    medians = []
    for i in xrange(l, r + 1, 5):
        temp = sorted(A[i:min(i+5, r+1)])
        medians.append(temp[len(temp) // 2])

    pivot = sorted(medians)[len(medians) // 2]
    pivot_index = l + A[l:r+1].index(pivot)

    # swap index p and r
    A[pivot_index], A[r] = A[r], A[pivot_index]

    return pivot
