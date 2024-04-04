def find_insert_position(arr, x):
    index = 0
    arrLength = len(arr)

    while index < arrLength:
        mid = (index + arrLength) // 2
        if arr[mid] < x:
            index = mid + 1
        else:
            arrLength = mid
    print(index)


array = [1, 2, 3, 3, 3, 5]
x = 4

find_insert_position(array, x)