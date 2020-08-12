# binary search tree is different than a binary tree

# Search rules:
#  left child's value must be < parent's value
# right child's value must be > parent's value

# for duplicates:
# not allow duplicate values in a BST
# pick a side, left or right, to also hold duplicate values (this method is what Sean uses)

# binary search tree running time
# logarithmic 0(log 2 n)
# intuitively, you can think of it as havling the iteration space per iteration

# BST                           Array:
# search: 0(log n)              search (unsorted): 0(n)
# insertion: 0(log n)           insertion: 0(1)
