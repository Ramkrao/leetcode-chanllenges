def identify_ranges(nums):
  result = []
  start = nums[0]
  end = nums[0]
  for i in range(1,len(nums)):
    if nums[i] == end + 1:
      end = nums[i]
    else:
      if start == end:
        result.append(str(start))
      else:
        result.append(f'{start}->{end}')
      start = end = nums[i]
  
  if start == end:
    result.append(str(start))
  else:
    result.append(f'{start}->{end}')
  
  return result


print(identify_ranges([0,1,2,4,5,7]))
print(identify_ranges([0,2,3,4,6,8,9]))