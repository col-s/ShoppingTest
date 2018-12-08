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
        sorted_numbers = sorted(numbers)
        if count % 2:
            return sorted_numbers[count//2]
        else:
            return sum(sorted_numbers[count//2-1:count//2+1]) / 2.0


# quicksort implementation for sorting list of numbers if
# pythons sorted() or list.sort() are not used
def sort_numbers(numbers):
    _quick_sort(numbers, 0, len(numbers) - 1)


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
