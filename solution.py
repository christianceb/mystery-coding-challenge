def solution(x, y):
    return 1

def sort(list):
    def partition(start, end):
        pivot_index = start
        store_index = pivot_index + 1 # The index where we swap the smaller number right next to pivot and co
        i = pivot_index + 1

        while i <= end:
            if list[i] < list[pivot_index]:
                list[store_index], list[i] = list[i], list[store_index]
                store_index += 1

            i += 1

        list[pivot_index], list[store_index - 1] = list[store_index - 1], list[pivot_index]

        return store_index

    def quick_sort(start, end):
        if start < end:
            pivot = partition(start, end)

            quick_sort(start, pivot - 1)
            quick_sort(pivot, end)

    quick_sort(0, len(list) - 1)

    return list

def merge_sort(list):
    """Merge sort, duh?
    :param list: List of things to sort
    :return: Cool sorted list
    """
    if len(list) > 1:
        middle = len(list) // 2
        left = merge_sort(list[:middle])  # Sort left partition
        right = merge_sort(list[middle:])  # Sort right partition

        list = []

        # As long as we have stuff to sort, we run this routine
        while len(left) > 0 and len(right) > 0:
            if left[0] == right[0]:
                list.append(right[0])

                left.pop(0)
                right.pop(0)
            elif left[0] < right[0]:
                list.append(left[0])
                left.pop(0)
            else:
                list.append(right[0])
                right.pop(0)

        # Merge left partition items to list
        for item in left:
            list.append(item)

        # and then the right
        for item in right:
            list.append(item)

    return list

def search(value, list):
    def binary_search(value, start, end):
        foundIndex = None

        if end >= start:
            middle = start + ( (end - start) // 2 )

            if list[middle] == value:
                foundIndex = middle
            elif value < list[middle]:
                foundIndex = binary_search(value, start, middle - 1)
            else:
                foundIndex = binary_search(value, middle + 1, end)
        
        return foundIndex

    index = binary_search(value, 0, len(list) - 1)

    return index

def diff(x, y):
    x = sort(x)
    y = sort(y)

    i = 0

    while i < len(x):
        found_y_index = search(x[i], y)

        if found_y_index != None:
            x.pop(i)
            y.pop(found_y_index)

            i -= 1

        i += 1

    return x + y