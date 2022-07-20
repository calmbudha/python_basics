'''
Find maxium sum of a subarray using Kadane algorithm
'''
import os

def kadane_sum(arr):
    local_sum = max_sum = 0
    for item in arr:
        local_sum = max(item, item + local_sum)
        if local_sum > max_sum:
            max_sum = local_sum
    return max_sum

def print_array(arr):
    for item in arr:
        print(item, end =' ')

if __name__ == "__main__":
    input_arr = input().rstrip().split()
    arr = []
    for item in input_arr:
        arr.append(int(item))
    res = kadane_sum(arr)
    print(res)

