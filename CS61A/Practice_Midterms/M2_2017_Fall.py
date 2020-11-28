
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


def splink(a, b, k):

    if b == Link.empty:
        return a
    elif k == 0 and b:
        return  Link(b.first, splink(a, b.rest, k))
    return Link(a.first, splink(a.rest, b, k-1))

"""Implement both, which takes two sorted linked lists composed of Link objects and returns whether
some value is in both of them. The Link class is defined on the midterm 2 study guide.
Important: You may not use len, in, for, list, slicing, element selection, addition, or list comprehensions."""
def both(a, b):
    if a == Link.empty or b == Link.empty:
        return False
    if a.first > b.first:
        a, b = b, a
    return a.first == b.first or both(a.rest, b)
def ways(start, end, k, actions):

    if start == end and k>= 0:
        return 1
    elif start != end and k < 0:
        return 0
    return sum([ways(f(start),end,k-1,actions) for f in actions])

print(ways(1, 10, 5, [lambda x: x+1, lambda x: x+4]))

def pile(t):
"""Return a dict that contains every path from a leaf to the root of tree t.
>>> pile(tree(5, [tree(3, [tree(1), tree(2)]), tree(6, [tree(7)])]))
{1: (3, (5, ())), 2: (3, (5, ())), 7: (6, (5, ()))}
"""
    p = {}
    def gather(u,def):
        if is_leaf(u):
            p[label(u)] = def
        for b in branches(u):
            gather(b, (label(b), def))
    gather(t,())
    return p

class Path:
"""A path through a tree from the root to a leaf, identified by its leaf label.
>>> a = tree(5, [tree(3, [tree(1), tree(2)]), tree(6, [tree(7)])])
>>> print(Path(a, 7), Path(a, 2))
5-6-7 5-3-2
"""
    def __init__(self, t, leaf_label):
        self.pile, self.end = pile(t), leaf_label
    def __str__(self):
        path, s = self.pile[self.end] , str(self.end)
        while path:
            path, s = path[1] , str(path[0]) + '-'+ s 
        return s
