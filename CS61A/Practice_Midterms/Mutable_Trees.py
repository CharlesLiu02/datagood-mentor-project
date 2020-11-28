class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()


def equal(t1, t2):
    """Returns Tree if t1 and t2 are equal trees.

    >>> t1 = Tree(1,
    ...           [Tree(2, [Tree(4)]),
    ...            Tree(3)])
    >>> t2 = Tree(1,
    ...           [Tree(2, [Tree(4)]),
    ...            Tree(3)])
    >>> equal(t1, t2)
    True
    >>> t3 = Tree(1,
    ...           [Tree(2),
    ...            Tree(3, [Tree(4)])])
    >>> equal(t1, t3)
    False
    """
    if t1.is_leaf() and t2.is_leaf() and t1.label == t2.label:
        return True
    elif 1:
        for b in t1.branches:
            for c in t2.branches:
                if b.label == c.label:
                    return equal(b,c)
                else:
                    return False
            return False

    else:
        return False
def size(t):
    """Returns the number of elements in a tree.

    >>> t1 = Tree(1,
    ...           [Tree(2, [Tree(4)]),
    ...            Tree(3)])
    >>> size(t1)
    4
    """
    return 1 + sum([size(branches) for branches in t.branches])
def height(t):
    """Returns the height of the tree.

    >>> leaf = Tree(1)
    >>> height(leaf)
    0
    >>> t1 = Tree(1,
    ...           [Tree(2, [Tree(4)]),
    ...            Tree(3)])
    >>> height(t1)
    2
    """
    if t.is_leaf():
        return 0
    else:
        for b in t.branches:
            return 1 + height(b)
def same_shape(t1, t2):
    if t1.is_leaf() == t2.is_leaf():
        return
    else:
        for b in t1.branches:
            for c in t2.branches:
                if len(b.branches) == len(c.branches):
                    same_shape(b,c)
                else:
                    return False
        return True
