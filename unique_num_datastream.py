unique = set()
ordered_unique = []
def add(num):
  if num not in unique:
    unique.add(num)
    ordered_unique.append(num)
  else:
    unique.remove(num)
    ordered_unique.remove(num)
  return

def showFirstUnique():
  if len(ordered_unique) > 0:
    print(ordered_unique[0])
  else:
    print(-1)


add(1)
showFirstUnique()
add(1)
showFirstUnique()
add(1)
showFirstUnique()
