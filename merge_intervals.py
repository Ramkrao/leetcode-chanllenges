import ast
# [[1,3],[2,6],[8,10],[15,18]]
# [[1,4],[4,5]]
def parse_str_to_array(s: str):
    lists = ast.literal_eval(s)
    return sorted(lists)


def merge_arrays(lst):
    new_seq = []
    new_arr = None
    for i, l in enumerate(lst):
        if new_arr:
            l = new_arr

        if (i != len(lst) - 1) and lst[i+1][0] >= l[0] and lst[i+1][0] <= l[1]:
            new_arr = ([l[0],lst[i+1][1]])
        else:
            new_seq.append(l)
            new_arr = None
    print(new_seq)

with open("input.txt") as file:
    for line in file:
        merge_arrays(parse_str_to_array(line.strip()))
