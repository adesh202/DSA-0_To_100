
def selection_sort(arr):
    # Selection sort
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Test the selection sort function
arr = [13, 46, 24, 52, 20, 9]
print("Before selection sort:", arr)
selection_sort(arr)
print("After selection sort:", arr)