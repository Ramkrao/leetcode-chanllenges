def find_sliding_windo_max(k, nums):
  output = []
  for i in range(len(nums) - k + 1):
    output.append(max(nums[i:i + k]))
  return output

print(find_sliding_windo_max(3, [1,3,-1,-3,5,3,6,7]))