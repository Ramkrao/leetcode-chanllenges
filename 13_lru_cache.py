class LRUCache:
  def __init__(self, depth):
    self.depth = depth
    self.cache = {}
    self.queue = []

  def get(self, key):
    if key in self.cache:
      self.queue.remove(key)
      self.queue.insert(0, key)
      return self.cache[key]  
    else:
      return -1
  
  def put(self, key, val):
    if len(self.cache.keys()) < self.depth or key in self.cache:
      self.cache[key] = val
    else:
      item = self.queue.pop()
      self.cache.pop(item)
      self.cache[key] = val
    if key in self.queue:
      self.queue.remove(key)
    self.queue.insert(0, key)

lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))      # returns 1
lru.put(3, 3)          # evicts key 2
print(lru.get(2))      # returns -1
lru.put(4, 4)          # evicts key 1
print(lru.get(1))      # returns -1
print(lru.get(3))      # returns 3
print(lru.get(4))      # returns 4
