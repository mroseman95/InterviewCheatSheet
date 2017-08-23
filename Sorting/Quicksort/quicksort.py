import time, random

def quicksort(A, l=None, r=None):
    """
    quicksort takes a list A and performs the quicksort algorithm on a sublist, and returns the resulting sublist sorted.
    @param A: A list of elements that can be compared to each other
    @param l: The leftmost index of the sublist
    @param r: The rightmost index of the sublist
    @return: A list that contains the same elements of A but in sorted order
    O(nlogn) where n is len(A) if quicksort median of medians is used, but O(n^2) if median of three is used
    but median of three is faster on average, because choosing a pivot is O(c) time instead of O(n) time
    like in median of median method
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
    O(n) + O(n) = O(n) where n = r - l
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
    O(n/5 * 5) = O(n) where n = r - l
    """
    #pivot = get_pivot_median_of_three(A, l, r)
    pivot = get_pivot_median_of_medians(A, l, r)
    pivot_index = l + A[l:r+1].index(pivot)

    # swap index p and r
    A[pivot_index], A[r] = A[r], A[pivot_index]

    return pivot

def get_pivot_median_of_three(A, l, r):
    """
    get_pivot_median_of_three takes a sublist of A and finds a pivot within it using the median of three method
    @param A: A list of elements that can be compared to each other
    @param l: the leftmost index of the sublist
    @param r: the rightmost index of the sublist
    @return: the valud of the pivot
    """
    # If there are less than 3 elements
    if r  + 1 - l <= 3:
        return sorted(A[l:r+1])[(r + 1 - l) // 2]

    random.seed(time.time())
    # the middle candidate is chosen from the sublist minus the first and last element
    candidate_2 = random.randrange(l+1,r)
    # if there is only one element to the left of the second candidate, make that the first candidate
    if candidate_2 - l == 1:
        candidate_1 = l
    else:
        candidate_1 = random.randrange(l, candidate_2)
    # if there is only one element to the right of the second candidate, make that the third candidate
    if r+1 - candidate_2 == 1:
        candidate_3 = r+1
    else:
        candidate_3 = random.randrange(candidate_2+1, r+1)

    candidate_values = sorted([A[candidate_1], A[candidate_2], A[candidate_3]])
    A[candidate_1] = candidate_values[0]
    A[candidate_2] = candidate_values[1]
    A[candidate_3] = candidate_values[2]

    return A[candidate_2]

def get_pivot_median_of_medians(A, l, r):
    """
    get_pivot_median_of_medians takes a sublist of A and finds a pivot within it using the median of medians method
    @param A: A list of elements that can be compared to each other
    @param l: the leftmost index of the sublist
    @param r: the rightmost index of the sublist
    @return: the value of the pivot
    """
    medians = []
    for i in xrange(l, r + 1, 5):
        temp = sorted(A[i:min(i+5, r+1)])
        medians.append(temp[len(temp) // 2])

    pivot = sorted(medians)[len(medians) // 2]

    return pivot
