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


def column(g, c):

    return [x[c] for x in g]

print(column([[3, 4, 5], [6, 7, 8], [9, 10, 11]], 1))



def stretch(s, repeat=0):
    if s != Link.empty:
        for i in range(repeat):
            s.rest = Link(s.first,s.rest)
            s = s.rest
        stretch(s.rest,repeat+1)

a = Link(3, Link(4, Link(5, Link(6))))
stretch(a)

def combo(a, b):
    if a == 0 or b == 0:
        return a + b
    elif a%10 == b%10:
        return combo(a//10, b//10) * 10 + a%10
    return min(combo(a,b//10) * 10 + b %10, combo(a//10, b) * 10 + a %10)
print(combo(531, 4321))

def siblings(t):
    result = [x.label for x in t.branches if len(t.branches) > 1]
    for b in t.branches:
        result = result + siblings(b)
    return result
a = Tree(4, [Tree(5), Tree(6), Tree(7, [Tree(8)])])
print (siblings(Tree(1, [Tree(3, [a]), Tree(9, [Tree(10)])])))

class Sib(Tree):
    def __init__(self, label, branches=[]):
        self.siblings = 0
        for b in branches:
            b.siblings += len(branches) -1
        Tree.__init__(self, label, branches)

a = Sib(4, [Sib(5), Sib(6), Sib(7, [Sib(8)])])
print(a.branches[1].siblings)
