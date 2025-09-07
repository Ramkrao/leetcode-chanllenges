def insert_intervals(intervals, new_interval):
  temp = None
  updated = []
  for u, v in intervals:
    interval = temp if temp else new_interval
    if (u <= interval[0] and interval[0] <= v) or (interval[0] <= u and u <= interval[1]):
      temp = [min(u,interval[0]), max(v,interval[1])]
    else:
      if temp:
        updated.append(temp)
        temp = None
      updated.append([u,v])

  return updated


print(insert_intervals([[1,3],[6,9]], [2,5]))
print(insert_intervals([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
