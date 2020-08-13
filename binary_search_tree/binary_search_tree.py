import sys
from collections import deque


class BSTNode:
    def __init__(self, value):
        # the value at the current node
        self.value = value
        # reference to this node's left child
        self.left = None
        # reference to this node's right child
        self.right = None

    def insert(self, value):
        # check if the new node's value is less than our current node's value
        if value < self.value:
            # if there's no left child here already, place the new node here
            if not self.left:
                self.left = BSTNode(value)
            else:
                # otherwise, repeat the process!
                self.left.insert(value)
        # check if the new node's value is greater than or equal to our
        # current node's value
        elif value >= self.value:
            # if there's no right child here already, place the new node here
            if not self.right:
                self.right = BSTNode(value)
            else:
                # otherwise, repeat the process!
                self.right.insert(value)

    def contains(self, target):
        # if the value of the current node we're looking at matches the target, we've found a match!
        if self.value == target:
            return True
        # if there's a left child, call its contains method to repeat the whole process
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        # if there's a right child, call its contains method to repeat the whole process
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    def get_max(self):
        # no point in doing anything if our tree is empty
        if not self:
            return None

        # Recursive approach
        # if not self.right:
        #   return self.value
        # return self.right.get_max()

        # initialize max_value variable; this will be updated as we traverse the tree
        max_value = self.value
        # get a reference to the node we're currently at; update this variable as we traverse the tree
        current = self
        # check to see if we're still at a valid tree node
        while current:
            # if current value is greater than max_value, update the max_value
            if current.value > max_value:
                max_value = current.value
            # move on to the next right node in the tree
            current = current.right
        return max_value

    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    def iterative_depth_first_for_each(self, cb):
        stack = []
        stack.append(self)

        while len(stack):
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)

    def breadth_first_for_each(self, cb):
        q = []
        q.append(self)

        while len(q):
            current_node = q.pop(0)
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            cb(current_node.value)

    # Pre-order DFT
    def pre_order_dft(self):
        if not self:
            return

        print(self.value)

        if self.left:
            self.left.pre_order_dft()

        if self.right:
            self.right.pre_order_dft()

    # In-order DFT (Can be used to copy the tree)
    def in_order_dft(self):
        if not self:
            return

        if self.left:
            self.left.in_order_dft()

        print(self.value)

        if self.right:
            self.right.in_order_dft()

    # Post-order DFT (Can be used to delete the tree)
    def post_order_dft(self):
        if not self:
            return

        if self.left:
            self.left.post_order_dft()

        if self.right:
            self.right.post_order_dft()

        print(self.value)

    def in_order_print(self):
        if not self:
            return

        if self.left:
            self.left.in_order_print()

        print(self.value)

        if self.right:
            self.right.in_order_print()

    # Graph Like BFT
    def bft_print(self):
        """
        Print each vertex in breadth-first order
        beginning from starting_node.
        """
        qq = deque()
        qq.append(self)

        while len(qq) > 0:
            current = qq.popleft()
            print(current.value)
            if current.left:
                qq.append(current.left)
            if current.right:
                qq.append(current.right)

    # Graph Like DFT
    def dft_print(self):
        """
        Print each vertex in breadth-first order
        beginning from starting_node.
        """
        s = []
        s.append(self)

        while len(s) > 0:
            current = s.pop()
            print(current.value)
            if current.left:
                s.append(current.left)
            if current.right:
                s.append(current.right)


# Testing
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()
