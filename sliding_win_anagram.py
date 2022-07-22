'''
Find all substrings of a string that are a permutation of another string
'''

from collections import Counter

def findAnagramsInString(s, sub_str):
    n_substr = len(sub_str)    
    n = len(s)
    count_substr = Counter(sub_str)
    
    # check if first substring is an anagram
    count_iter = Counter(s[0:n_substr])
    if count_substr == count_iter:
            print("Anagram '", end="")
            print(s[begin:begin+n_substr], end="")
            print("' present at index", begin)
    
    # start iterating through the string
    begin = 1
    while begin <= n - n_substr:
        count_iter[s[begin-1]] -= 1
        count_iter[s[begin + n_substr - 1]] += 1
        if count_substr == count_iter:
            print("Anagram '", end="")
            print(s[begin:begin+n_substr], end="")
            print("' present at index", begin)
        begin += 1
    return


if __name__ == "__main__":
    s = input().rstrip().lstrip()
    sub_str = input().rstrip().lstrip()

    findAnagramsInString(s, sub_str)

