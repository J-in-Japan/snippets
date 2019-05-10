# Implement locking in a binary tree. A binary tree node can be 
# locked or unlocked only if all of its descendants or ancestors are not locked.

# Design a binary tree node class with the following methods:

# is_locked, which returns whether the node is locked
# lock, which attempts to lock the node. If it cannot be locked, 
  # then it should return false. Otherwise, it should lock it and return true.
# unlock, which unlocks the node. If it cannot be unlocked, 
  # then it should return false. Otherwise, it should unlock it and return true.

# You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.

class node:
    def __init__(self, locked: bool=False):
        self.locked = locked
        self.parent = None
        self.left = None
        self.right = None
    def has_locked_node(self) -> bool:
        found_locked = False
        if self.locked:
            return True
        if self.left:
            if self.left.has_locked_node():
                found_locked = True
        if self.right:
            if self.right.has_locked_node():
                found_locked = True
        
        return found_locked
    def lock(self) -> bool:
        if self.locked:
            return True
        able_to_lock = False
        if self.left:
            able_to_lock = self.left.lock()
        if not able_to_lock:
            return False
        if self.right:
            able_to_lock = self.right.lock()
        if not able_to_lock:
            return False
        return True
    def unlock(self) -> bool:
        if not self.locked:
            return True
        if self.left.has_locked_node():
            self.left.unlock()

root = node()
root.left = node(True)
root.right = node()

print(root.has_locked_node())