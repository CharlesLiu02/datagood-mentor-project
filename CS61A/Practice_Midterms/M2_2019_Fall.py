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
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
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

def max_tree(t, key):
    """Return the label n of t for which key(n) returns the largest value.
    >>> t = Tree(6, [Tree(3, [Tree(5)]), Tree(2), Tree(4, [Tree(7)])])
    >>> max_tree(t, key=lambda x: x)
    7
    >>> max_tree(t, key=lambda x: -x)
    2
    >>> max_tree(t, key=lambda x: -abs(x - 4))
    4
    """
    if t.is_leaf():
        return t.label
    x = t.label
    for b in t.branches:
        m = max_tree(b,key)
        if m >= x:
            x = m
    return x


def max_tree(t, key):
    "Return the label n of t for which key(n) returns the largest value."
    return max([[y.label for y in x.branches] for x in t.branches], key=key)




def stable(s, k, n):
    """Return whether all pairs of elements of S within distance K differ by at most N.
    >>> stable([1, 2, 3, 5, 6], 1, 2) # All adjacent values differ by at most 2.
    True
    >>> stable([1, 2, 3, 5, 6], 2, 2) # abs(5-2) is a difference of 3.
    False
    >>> stable([1, 5, 1, 5, 1], 2, 2) # abs(5-1) is a difference of 4.
    False
    """
    for i in range(len(s)):
        near = range(i-k+1, i+k+1)
        if any([(abs(s[i] - s[j])) > n for j in near]):
            return False
        return True

def partitions(n, m):
    """Yield all partitions of N using parts up to size M.
    >>> list(partitions(1, 1))
    ['1']
    >>> list(partitions(2, 2))
    ['2', '1 + 1']
    >>> list(partitions(4, 2))
    ['2 + 2', '2 + 1 + 1', '1 + 1 + 1 + 1']
    >>> for p in partitions(6, 4):
    ... print(p)
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """
    if m == 1:
        yield n
    if n > 0 and m > 0:
        for p in partitions(n, n-m):
            yield str(n) + ' + ' + str((n-m))
        yield from partitions(n-1, m)
list(partitions(4, 2))

def switch(s, t, k):
    """Return the list with the largest sum built by switching between S and T at most K times.
    >>> switch([1, 2, 7], [3, 4, 5], 0)
    [1, 2, 7]
    >>> switch([1, 2, 7], [3, 4, 5], 1)
    [3, 4, 5]
    >>> switch([1, 2, 7], [3, 4, 5], 2)
    [3, 4, 7]
    >>> switch([1, 2, 7], [3, 4, 5], 3)
    [3, 4, 7] """
    if k == 0 or len(s) == 0:
        return s
    else:
        a = switch(t, s, k-1)
        b = s[:1] + switch(s[1:], t[1:], k-1)
    return max(a, b, key=sum)

print(switch([1, 2, 7], [3, 4, 5], 1))

class Version:
    """A version of a string after an edit.
    >>> s = Version('No power?', Delete(3, 6))
    >>> print(Version(s, Insert(3, 'class!')))
    No class!
    >>> t = Version('Beary', Insert(4, 'kele'))
    >>> print(t)
    Bearkeley
    >>> print(Version(t, Delete(2, 1)))
    Berkeley
    >>> print(Version(t, Delete(4, 5)))
    Bear
    """
    def __init__(self, previous, edit):
        self.previous, self.edit = previous, edit
    def __str__(self):
        return str(self.edit.apply(str(self.previous)))

class Edit:
    def __init__(self, i, c):
        self.i, self.c = i, c

class Insert(Edit):
    def apply(self, t):
        "Return a new string by inserting string c into t starting at position i."
        return str(t[0:self.i]) + str(self.c) + str(t[self.i:])

class Delete(Edit):
    def apply(self, t):
        "Return a new string by deleting c characters from t starting at position i."
        return str(t[0:self.i]) + str(t[(self.i+self.c):])


def layer(t, d):
    """Return a linked list containing all labels of Tree T at depth D.
    >>> a_tree = Tree(1, [Tree('b', [Tree('mas')]),
    ... Tree('a', [Tree('co')]),
    ... Tree('d', [Tree('t', [Tree('!')])])])
    >>> print(layer(a_tree, 0))
    <1>
    >>> print(layer(a_tree, 1))
    <b a d>
    >>> print(layer(a_tree, 2))
    <mas co t>
    >>> print(layer(a_tree, 3))
    <!>
    """
    return helper(t, d, Link.empty)

def helper(t, d, s):
    if d == 0:
        return Link(t.label,s)
    else:
        for b in reversed(t.branches):
            s = helper(b,d-1,s)
    return s


a_tree = Tree(1, [Tree('b', [Tree('mas')]), Tree('a', [Tree('co')]), Tree('d', [Tree('t', [Tree('!')])])])
print(layer(a_tree, 0))
print(layer(a_tree, 2))
