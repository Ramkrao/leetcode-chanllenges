# [1,1,1,2,2,3], k = 2

def top_k_freq(arr, k):
    vals = {}
    for el in arr:
        if el in vals:
            vals[el] += 1
        else:
            vals[el] = 1
    count_arr = sorted(vals.items(), key=lambda item: item[1], reverse=True)
    ret = []
    for a in count_arr[:k]:
        ret.append(a[0])
    return ret

print(top_k_freq([1,1,1,2,2,3],2))
print(top_k_freq([4,1,-1,2,-1,2,3], k = 2))
