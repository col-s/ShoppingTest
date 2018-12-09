def get_median(numbers):
    """
    helper function to calculate median assuming
    numpy median() function is not used
    :arg numbers: list of ints or floats
    """
    count = len(numbers)
    if count == 0:
        return None
    else:
        # preform the sort on a copy of the list so as not to alter original list
        sorted_numbers = sort_numbers(numbers, copy=True)
        if count % 2:
            return sorted_numbers[count//2]
        else:
            return sum(sorted_numbers[count//2-1:count//2+1]) / 2.0


def sort_numbers(numbers, copy=False):
    """
    quicksort implementation for sorting list of numbers if
    pythons sorted() or list.sort() methods are not used
    :arg numbers: list of ints or floats
    :arg copy: bool to determine list whether a copy of the list is returned
        or it is mutated in place, and None is returned
    """
    list_to_sort = numbers
    if copy:
        list_to_sort = list(numbers)
    _quick_sort(list_to_sort, 0, len(numbers) - 1)
    if copy:
        return list_to_sort


def _quick_sort(numbers, left, right):
    if left >= right:
        return
    # picking the middle index in the list as the pivot
    pivot = numbers[(left + right) // 2]
    # get the new index
    index = _partition(numbers, left, right, pivot)
    _quick_sort(numbers, left, index - 1)
    _quick_sort(numbers, index, right)


def _partition(numbers, left, right, pivot):
    while left <= right:
        while numbers[left] < pivot:
            left += 1
        while numbers[right] > pivot:
            right -= 1
        if left <= right:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1
            right -= 1
    return left
