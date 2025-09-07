# pwwkew
def findValue(str):
    temp = [str[0]]
    for s in str:
        if s not in temp:
            temp.append(s)
        for i, t in enumerate(temp):
            if s not in t:
                temp[i] = temp[i] + s
    longest = max(temp, key=lambda item: len(item)) 
    print(longest)

def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    longest = 0
    start = 0  # start index of current window

    for i, char in enumerate(s):
        # If char is already in the current window, move start to the right of its previous index
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        
        char_index_map[char] = i
        longest = max(longest, i - start + 1)
        print(char_index_map, start, longest)

    return longest

with open("input.txt") as f:
    for line in f:
        # findValue(line.strip())
        print(length_of_longest_substring(line.strip()))
