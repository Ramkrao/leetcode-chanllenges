def rotate(matrix):
  n = len(matrix)

  for i in range(n):
    for j in range(i+1, n):
      print(i,j)
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

  for row in matrix:
    row.reverse()
  print(matrix)

rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
])