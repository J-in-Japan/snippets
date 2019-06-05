# preorder traversal
# [a, b, d, e, c, f, g]
# inorder traversal
# [d, b, e, a, f, c, g]
# should return
#      a
#   b     c
#  d e   f g

class tree:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

pre = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
ino = ['d', 'b', 'e', 'a', 'f', 'c', 'g']

# root = pre[0]
# left_side = []
# right_side = []
# root_index = 100
# for i in ino:
#     if ino[i] != root and i < root_index:
#         left_side.append(ino[i])
#     elif ino[i] == root:
#         root_index = i
#     else:
#         right_side.append(ino[i])


# def build_a_tree(pre: list, ino: list) -> tree:
#     if len(pre) == 0:
#         return None
    
#     root_val = pre[0]
#     root_ind = ino.index(root_val)

#     ino_left = ino[0:root_ind]
#     ino_right = ino[root_ind:]

#     root = tree(root_val)
#     root.left = build_a_tree(pre[1:], )





# def build_tree(ino, pre, ino_start, ino_end):
#     if ino_start > ino_end:
#         return None
    
#     # pick next node from left side of preorder
#     n = tree(pre[0])

#     for p in range(len(pre)):
#         ino


def build_tree(in_order, pre_order, in_strt, in_end): 
      
    if (in_strt > in_end): 
        return None
  
    # Pich current node from Preorder traversal using 
    # preIndex and increment preIndex 
    n = tree(pre_order[build_tree.pre_index]) 
    build_tree.pre_index += 1
  
    # If this node has no children then return 
    if in_strt == in_end : 
        return n 
  
    # Else find the index of this node in Inorder traversal 
    in_index = search(in_order, in_strt, in_end, n.val) 
      
    # Using index in Inorder Traversal, construct left  
    # and right subtrees 
    n.left = build_tree(in_order, pre_order, in_strt, in_index-1) 
    n.right = build_tree(in_order, pre_order, in_index + 1, in_end) 
  
    return n 
  
# UTILITY FUNCTIONS 
# Function to find index of vaue in arr[start...end] 
# The function assumes that value is rpesent in inOrder[] 
  
def search(arr, start, end, value): 
    for i in range(start, end + 1): 
        if arr[i] == value: 
            return i 
  
def print_inorder(node): 
    if node is None: 
        return 
      
    # first recur on left child 
    print_inorder(node.left) 
      
    # then print the data of node 
    print(node.val) 
  
    # now recur on right child 
    print_inorder(node.right) 
      
# Driver program to test above function 
in_order = ['D', 'B', 'E', 'A', 'F', 'C'] 
pre_order = ['A', 'B', 'D', 'E', 'C', 'F'] 
# Static variable preIndex 
build_tree.pre_index = 0
root = build_tree(in_order, pre_order, 0, len(in_order)-1) 
  
# test the build tree by priting Inorder traversal 
print(f"Inorder traversal of the constructed tree is {print_inorder(root)}")
