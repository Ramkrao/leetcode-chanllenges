def find_min_coins(amount, coins):
  coins_reverse = sorted(coins)
  coins_reverse.reverse()
  count = 0
  possibilities = []
  for i in range(len(coins_reverse)):
    temp_amount = amount
    for coin in coins_reverse[i:]:
      while temp_amount >= coin:
        temp_amount -= coin
        count += 1
      if temp_amount == 0:
        possibilities.append(count)
        count = 0
        break
  if len(possibilities) == 0:
    return -1
  return min(possibilities)


print(find_min_coins(11, [1,2,5]))
print(find_min_coins(3, [2]))
print(find_min_coins(6, [1,3,4]))