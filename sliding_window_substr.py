'''
Find the longest substring of a string containing `k` distinct characters
'''

def findLongestSubStr(s, k):
    # map to store recurrences within substr
    counter = {}
    
    # longest substr begin and end
    begin = end = 0

    # iterators for window
    low = high = 0

    while high < len(s):
        if s[high] in counter.keys():
            counter[s[high]] += 1
        else:
            counter[s[high]] = 1

        # if length of window is more than k, remove first element
        while len(counter.keys()) > k:
            counter[s[low]] -= 1
            if counter[s[low]] == 0:
                counter.pop(s[low])
            low += 1

        if end - begin < high - low:
            end = high
            begin = low

        high += 1
    return s[begin:end+1]



if __name__ == '__main__':
 
    s = input().rstrip()
    k = int(input().rstrip())
 
    print(findLongestSubStr(s, k))
