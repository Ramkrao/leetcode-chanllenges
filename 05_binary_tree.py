class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Parser:
  def serialise(self, root):
    def preorder(node):
      if not node:
        vals.append('null')
        return
      vals.append(str(node.val))
      preorder(node.left)
      preorder(node.right)

    vals = []
    preorder(root)
    return ','.join(vals)
  
  def deserialise(self, data):
    def build():
      val = next(vals)
      if val == 'null':
        return None
      node = TreeNode(int(val))
      node.left = build()
      node.right = build()
      return node

    vals = iter(data.split(','))
    return build()
  
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

serialised = Parser().serialise(root)
print(serialised)

print(Parser().deserialise(serialised).val)
