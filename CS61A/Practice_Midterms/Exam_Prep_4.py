def splink(a, b, k):
"""Return a Link containing the first k elements of a, then all of b, then the rest of a.
>>> splink(Link(2, Link(3, Link(4, Link(5)))), Link(6, Link(7)), 2)
Link(2, Link(3, Link(6, Link(7, Link(4, Link(5))))))
"""
    if k == 0 and not b:
        return a
    elif k == 0 and b:
        return  splink(a,b.rest)
    return splink(a, b, k-1)

def tree(label, branches=[]):

    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):

    return tree[0]

def branches(tree):

    return tree[1:]

def is_tree(tree):

    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

"""A quant firm has enlisted your help in maximizing their trade profits. You know ahead of time how much
profit you will make by executing each trade. These values are stored in a tree (i.e., every node’s value
corresponds to the profit you earn by making a certain trade). However, if you decide to trade a stock
represented by some node S, you are not allowed to execute trades that have an edge directly connected
to S (i.e., if you earn profit S, you cannot earn the profit from the parent or children of S). For example,
in the following tree (see below), if I choose to execute the trade corresponding to the node 4, then I earn
$4, but I cannot trade the stock corresponding to the 2, the 7, or the 8, since all 3 of these are connected
to 4.
Return the maximum profit you can make based on these constraints. The maximum you can make from
the tree below is $52 (3 + 9 + 10 + 11 + 7 + 12). Note that none of these selected profits have direct
edges to each other.
FYI: assume you have access to left and right, which are functions that select the left and right
subtrees of a given tree. They return None if the requested subtree does not exist. Also assume each node
has at most 2 children.
Challenge (out of scope for 61A): solve this in one post-order traversal without memoization."""
def profit(tree):
    return helper(tree, False)
def helper(tree, z):
    if tree is None:
        return 0
    if is_leaf(tree):
        return label(tree) if not z else 0
    if z == False:
        x = max(label(tree) + helper(left(tree),True), label(tree) + helper(right(tree),True))
        y = max(helper(right(tree), False), helper(left(tree), False))
        return max(x,y)
    else:
        return max(helper(left(tree), False), helper(right(tree), False))
pls = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
profit(pls)

"""The leaves in our trees are looking for love and would like to mingle with each other. However, they
can only contact other leaves that are within a distance of k, where k is the fewest number of edges that
connect one leaf to another. Return the number of leaf pairs in the tree that are separated by ≤ k edges.
For example, for k = 4 in the following tree, the function should return 4, since there are 4 pairs that are
within k edges of each other (10 and 11, 7 and 12, 9 and 10, 9 and 11). FYI: assume you have access to
left and right, which are functions that select the left and right subtrees of a given tree. They return
None if the requested subtree does not exist. Also assume each node has at most 2 children."""
def pairs(tree, k):
    def helper(tree, k):
        if tree is None:
            return [{}, 0]
        if is_leaf(tree):
            return [ret, 1]
        left, total_left = helper(left(tree),k-1) + helper(right(tree), k-1)
        right, total_right = helper(right(tree), k-1) + helper(left(tree),k-1)
        total = total_left + total_right
        for depth in left:
            for i in range(_______________________________________________________):
                total += _______________________________________________________
        ret = {}
        for key in left:
            _______________________________________________________
        for key in right:
            _______________________________________________________
        return [ret, total]
    return helper(tree, k)[1]
"""The lowest common ancestor of two nodes p and q is the lowest node in the tree from which both p and
q can be reached. For example, in the following tree, the lowest common ancestor of 10 and 11 is 6. The
lowest common ancestor for 9 and 6 is 3. The lowest common ancestor of 4 and 12 is 4. Assume all values
in the tree are unique, and return the value associated with the lowest common ancestor of p and q. FYI:
assume you have access to left and right, which are functions that select the left and right subtrees of
a given tree. They return None if the requested subtree doesn’t exist. Also assume each node has at most
2 children"""

def lowestCommonAncestor(tree, p, q):
    L = helper(left(tree), p, q)
    if L and L[1]:
        return L[0]
    R = helper(right(tree), p, q)
    if R and R[1]:
        return R[0]
    return label(tree)

def helper(tree, p, q):
    if tree is None:
        return
    if is_leaf(tree) and (label(tree) in [p,q]):
        return [label(trees),False]
    L, R = helper(left(tree), p, q), helper(right(tree), p, q)
    if label(tree) in [p, q]:
        return [label(tree), not (L is None and R is None)]
    if not R and L:
        return L
    if L and (L[1] or not R):
        return [label(tree), True]
    if not L and R:
        return R
