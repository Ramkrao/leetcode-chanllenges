def count_components(n, edges):

  def dfs(node):
    for neighbour in adj[node]:
      if neighbour not in visited:
        visited.add(neighbour)
        dfs(neighbour)

  adj = {i: [] for i in range(1,n+1)}
  
  for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

  visited = set()
  count = 0

  for node in range(1,n+1):
    if node not in visited:
      visited.add(node)
      dfs(node)
      count += 1

  print(adj, visited, count)

def count_components_union(k ,edges):
  parent = [i for i in range(k+1)]

  def find(x):
    if parent[x] != x:
      parent[x] = find(parent[x])
    return parent[x]

  def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
      parent[rootY] = rootX

  for u, v in edges:
    union(u, v)

  print(len({find(i) for i in range(1,k+1)}))

count_components(5,[[1,2],[2,3],[4,5]])
