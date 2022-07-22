'''
Find the longest substring of a string containing distinct characters
'''

def longestDistinctSubStr(s):
    # map to store recurrences within substr
    counter = {}    
    # longest substr begin and end
    begin = end = 0
    # iterators for window
    low = high = 0

    while high < len(s):
        if s[high] not in counter.keys():
            counter[s[high]] = 1
        else:
            index = s.find(s[high], low, high)
            for iter in range(low, index):
                counter.pop(s[iter])
            low = index+1
        # assign current substring to longest substring if it is longer        
        if end-begin < high-low:
            end = high
            begin = low
        
        high += 1

    return s[begin:end+1]


if __name__ == '__main__':
 
    s = input().rstrip().lstrip()

    print(longestDistinctSubStr(s))