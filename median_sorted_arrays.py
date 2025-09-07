import ast

def merge_and_median(lst):
    transform_lst = ast.literal_eval(lst)
    concat = [item for subarr in transform_lst for item in subarr]
    new_lst = sorted(concat)

    arr_len = len(new_lst)
    if arr_len %2 == 0:
        return (new_lst[arr_len // 2 - 1] + new_lst[arr_len // 2]) / 2
    else:
        return (new_lst[arr_len // 2])

with open("input.txt") as file:
    for line in file:
        print(merge_and_median(line.strip()))
        