# find the second largest value in a binary search tree
# max is easy to find -> furthest right leaf node (or root if no right)
# so basically need to find the next smallest

# my idea:
# keep a stack of items visited in finding the max then walk back

class bs_tree:
    def __init__(self, val: int=None):
        self.left = None
        self.right = None
        self.val = val
    def find_max_val(self) -> int:
        if self.right:
            return self.right.find_max_val()
        else:
            return self.val
    def find_max2(self, max):
        prev_node = None
        cur_node = self
        while cur_node.val != max:
            if cur_node.right:
                if cur_node.right.val < max:
                    cur_node = cur_node.right
    # would be good practice to implement insert (and search)
    def insert(root, node):
        if root is None:
            root = node
        else:
            if root.val < node.val:
                if root.right is None:
                    root.right = node
                else:
                    root.right.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    root.left.insert(root.left, node)

# A utility function to do inorder tree traversal 
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right) 
def revorder(root):
    if root:
        revorder(root.right)
        print(root.val)
        revorder(root.left)

  
# Driver program to test the above functions 
# Let us create the following BST 
#      50 
#    /      \ 
#   30     70 
#   / \    / \ 
#  20 40  60 80 
#r = Node(50) 
#insert(r,Node(30)) 
#insert(r,Node(20)) 
#insert(r,Node(40)) 
#insert(r,Node(70)) 
#insert(r,Node(60)) 
#insert(r,Node(80)) 
  
# Print inoder traversal of the BST 
#inorder(r) 

bs = bs_tree(8)
bs.left = bs_tree(3)
bs.left.left = bs_tree(1)
bs.left.right = bs_tree(6)
bs.left.right.left = bs_tree(4)
bs.left.right.right = bs_tree(7)
bs.right = bs_tree(10)
bs.right.right = bs_tree(14)
bs.right.right.left = bs_tree(13)
print(bs.find_max_val())

max2 = None
stack = list()
cur_node = bs
while cur_node.right:
    stack.append(cur_node)
    cur_node = cur_node.right
if cur_node.left:
     max2 = cur_node.left.find_max_val()
else:
    max2 = stack.pop().val

print(max2)

print('inorder')
inorder(bs)
print('revorder')
revorder(bs)

max_vals = list()
def quick_max2(root):
    if len(max_vals) >= 2:
        return
    if root:
        quick_max2(root.right)
        max_vals.append(root.val)
        quick_max2(root.left)

print(max_vals)
quick_max2(bs)
print(max_vals)