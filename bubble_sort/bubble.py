def bubble_sort(array):
    for _ in range (0, len(array)):
        for j in range(0, len(array) - 1):
            if (array[j+1] < array[j]):
                array[j+1], array[j] = array[j], array[j+1]
    print(array)

def main():
    arr = [3, 4, 7, 8, 21, 0]
    bubble_sort(arr)

main()