# Print the three most common characters along with their occurrence count each on a separate line.
# Sort output in descending order of occurrence count. 
# If the occurrence count is the same, sort the characters in alphabetical order. 

from collections import Counter

if __name__ == '__main__':
    s = sorted(input().strip())
    c = Counter(s).most_common(3)
    [print(key, value) for key, value in c]