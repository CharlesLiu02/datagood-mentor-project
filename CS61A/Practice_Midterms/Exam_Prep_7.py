class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                     Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                              Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
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
def node_func_gen(t, f, g):
    """
    >>> f = lambda x: x % 2 == 1
    >>> g = lambda x: x**2
    >>> for func in node_func_gen(t1, f, g)  note: order doesn't matter
    ... print(func(t1))
    ...
    1
    25
    9
    49
    """
    if f(t.label):
        yield lambda x: g(x.label)



def fib_tree(n):
    """
    >>> t = fib_tree(6)
    >>> t.label
    8
    >>> t.branches[0].label
    5
    >>> t.branches[1].label
    3
    """
    if n == 1 or n == 2:
        return Tree(1)
    return Tree(fib_tree(n-1).label + fib_tree(n-2).label, [fib_tree(n-1), fib_tree(n-2)])

t = fib_tree(6)
print(t.label)


def subsequences(lst):
    """
    >>> for seq in subsequences([1, 2, 3])  note: order doesn't matter
    ... print(seq)
    ...
    [1, 2, 3]
    [1, 2]
    [1, 3]
    [1]
    [2, 3]
    [2]
    [3]
    []
    """
    if lst != []:
        yield from map(lambda x: [lst[0]] + x, subsequences(lst[1:]))
        yield from subsequences(lst[1:])
    else:
        yield []

for seq in subsequences([1, 2, 3]):
    print(seq)



def black_hole(seq,trap):
    for x in seq:
        if x == trap:
            yield from generate_constant(x)
        else:
            yield x


def connect_consultant(t,v1,v2):
    def helper(t, v1,v2, v1_spotted):
        if t.label == v2 and v1_spotted:
            return True
        v1_spotted = v1_spotted or t.label == v1
        for b in t.branches:
            if helper(b,v1,v2, v1_spotted):
                return True
        return False
    return helper(t,v1,v2, )


def prune_tree(t,total):
    t.branches = [x for x in t.branches if x.label <= (total - t.label)]
    for b in t.branches:
         prune_tree(b,total-t.label)

def replace(s,t,i,j):
    if i > 1:
         replace(s.rest,t,i-1,j-1)
    else:
         for k in range(j - i):
             s.rest = s.rest.rest
         end = t
         while end != Link.empty:
             end = end.rest
         s.rest, end.rest = t, s.rest

def double_up(s):
    """
    Mutate s by inserting elements so that each element is next to an equal.
    Use Link class in Midterm 2 study guide.

    >>> s = Link(3, Link(4))
    >>> double_up(s)     Inserts 3 and 4
    2
    >>> s
    Link(3, Link(3, Link(4, Link (4))))
    >>> t = Link(3, Link(4, Link(4, Link (5))))
    >>> double_up(t)  Inserts 3 and 5
    2
    >>> t
    Link (3, Link(3, Link(4, Link(4, Link(5, Link(5))))))
    >>> u = Link(3, Link(4, Link(3)))
    >>> double_up(u)     Inserts 3 , 4 , and 3
    3
    >>> u
    Link(3, Link(3, Link(4, Link(4, Link(3, Link(3))))))
    """
    if s is Link.empty:
        return 0
    elif s.rest is Link.empty:
        s.rest = Link(s.first,s.rest)
        return 1
    elif s.first == s.rest.first:
        return double_up(s.rest.rest)
    else:
        s.rest = Link(s.first,s.rest)
        return 1 + double_up(s.rest.rest)
s = Link(3, Link(4))
u = Link(3, Link(4, Link(3)))
print(double_up(u))
print(u)
