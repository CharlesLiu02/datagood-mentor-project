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

def layer_gen(t):
    """
    >> lg = layer_gen(t1)
    >>> for node_label in lg:
    ... print(nodel_label)
    1
    2
    3
    4
    5
    6
    7
    8
    """

    visit = [t]
    while visit:
        node = visit.pop(0)
        yield node.label
        visit.extend(node.branches)

t1 = Tree(1, [Tree(2, [Tree(5), Tree(6, [Tree(8)])]), Tree(3), Tree(4, [Tree(7)])])


def fib_gen():
    """
    >>> fg = fib_gen()
    >>> for _ in range(10):
    ... print(next(fg))
    0
    1
    1
    2
    3
    5
    8
    13
    21
    34
    """
    yield from [0,1]
    a = fib_gen()
    next(a)
    for i in range(a):
        b.append()



def partition_gen(n):
    """
    >>> for partition in partition_gen(4): # note: order doesn't matter
    ... print(partition)
    [4]
    [3, 1]
    [2, 2]
    [2, 1, 1]
    [1, 1, 1, 1]
    """
    def yield_helper(j, k):
        if j == 0:
            yield []
        elif j > 0 and k> 0:
            for p in yield_helper(j-k,k):
                yield [k] + p
            yield from yield_helper(j,k-1)
    yield from yield_helper(n,n)

for partition in partition_gen(4):
    print(partition)
