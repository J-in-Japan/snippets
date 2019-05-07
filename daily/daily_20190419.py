#Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
#For example, given the following Node class

class Node: 
    def __init__(self, val, left=None, right=None): 
        self.val = val 
        self.left = left 
        self.right = right 
    
    def serialize(self, sentinel='#'):
        serial = [self.val]
        if self.left is None:
            serial.append(sentinel)
        else:
            serial.extend(self.left.serialize(sentinel))
        if self.right is None:
            serial.append(sentinel)
        else:
            serial.extend(self.right.serialize(sentinel))
        return serial

    @classmethod
    def deserialize(cls, source, sentinel='#'):
        def _helper(index):
            if source[index] == sentinel:
                return None, index + 1

            value = source[index]
            left, index = _helper(index + 1)
            right, index = _helper(index)
            return cls(value, left, right), index
        return _helper(0)[0]

if __name__ == "__main__":
#The following test should pass:
    node = Node('root', Node('left', Node('left.left')), Node('right')) 
    ser = node.serialize()
    print(ser)
    node2 = Node.deserialize(ser)
    #assert deserialize(serialize(node)).left.left.val == 'left.left'