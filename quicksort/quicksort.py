def quicksort(array):
    """  """
    if (len(array) <= 1):
        return array
    else:
        return quicksort([n for n in array[1:] if n < array[0]]) \
        + [array[0]] + quicksort([n for n in array[1:] if n >= array[0]])


array = [1, 5, 6, 9, 3, 2, 32, 77]
print(quicksort(array))