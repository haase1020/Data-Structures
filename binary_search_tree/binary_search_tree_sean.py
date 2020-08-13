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


##### Day 4 notes################
# Recursion
# Criteria -->
# 1. criteria that tells us when to stop traversing (base case)
# 2. some way to "move towards" one of the stopping cirteria
# 3. a starting point

# non-recursive fn: (iterative)
def search(arr, target):
    for n in arr:
        if n == target:
            return True
    return False

# recursive fn:


def search(arr, target):
    if len(arr) == 0:
        return False
    if arr[-1] == target:
        return True
    return search(arr[:-1])  # include everything but last item

    search([15, 27, 3, 16, 14, 19, 22], 3)
