'''

Dutch sort algorithm
dutch_sort sortes array with only 0, 1, and 2 
dnf_sort sorts an array with three distinct elements

'''



def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def print_array(arr):
    for item in arr:
        print(item, end =' ')
    print("\n")


def dutch_sort(arr):
    high = len(arr) - 1
    low = mid = 0

    while mid <= high:
        if arr[mid] == 0:
            swap(arr, low, mid)
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            swap(arr, mid, high)
            high -= 1
    return arr


def partition(arr, low, high):
    if high - low <= 1:
        if arr[high] <= arr[low]:
            swap(arr, high, low)
        return
    mid = low
    pivot = arr[high]
    while mid <= high:
        if arr[mid] < pivot:
            swap(arr, low, mid)
            low += 1
            mid += 1
        elif arr[mid] == pivot:
            mid+= 1
        elif arr[mid] > pivot:
            swap(arr, mid, high)
            high -= 1


def dnf_sort(arr, low, high):
    if low >= high:
        return
    
    partition(arr, low, high)


if __name__ == "__main__":
    input_arr = input().rstrip().split()
    arr = []
    for item in input_arr:
        arr.append(int(item))
    
    n = len(arr)
    res = dutch_sort(arr)
    # res = dnf_sort(arr, 0, n-1)
    print_array(arr)
