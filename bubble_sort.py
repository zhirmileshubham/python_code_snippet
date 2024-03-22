# Bubble Sort Algorithm

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [12, 1, 15, 8, 19, 50, 24, 99]
sorted_arr = []
sorted_arr = bubble_sort(arr)
print(f'Bubble sort of {arr}', sorted_arr)