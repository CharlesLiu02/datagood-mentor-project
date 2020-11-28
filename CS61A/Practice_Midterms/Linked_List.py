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
###Albert's Questions

def validate(lst):
    """Returns True if lst is a valid Link.

    >>> lst = Link(1, Link(2, Link(3)))
    >>> validate(lst)
    True
    >>> okay = Link(Link(1), Link(2))
    >>> validate(okay)
    True
    >>> bad = Link(1, 2)
    >>> validate(Link.empty)
    True
    """
    if lst.rest == Link.empty:
        return True
    elif type(lst.rest) is not Link:
        return False
    return validate(lst.rest)

def count(r, value):
    """Counts the number of times VALUE shows up in R.

    >>> r = Link(3, Link(3, Link(2, Link(3))))
    >>> count(r, 3)
    3
    >>> count(r, 2)
    1
    """
    counter = 0
    while r is not Link.empty:
        if r.first == value:
            counter += 1
            r = r.rest
        else:
            r=r.rest
    return counter

def extend_link(s1, s2):
    """Extends s1 to include the elements of s2.

    >>> s1 = Link(1)
    >>> s2 = Link(2, Link(3))
    >>> extend_link(s1, s2)
    >>> s1
    Link(1, Link(2, Link(3)))
    >>> s1.rest is not s2
    True
    """
    if s2 == Link.empty:
        return
    elif s1.rest != Link.empty:
        return extend_link(s1.rest, s2)
    else:
        s1.rest = Link(s2.first)
        return extend_link(s1, s2.rest)

def deep_map(fn, lst):
    """Applies FN to every element in lst.

    >>> normal = Link(1, Link(2, Link(3)))
    >>> deep_map(lambda x: x*x, normal)
    >>> normal
    Link(1, Link(4, Link(9)))
    >>> nested = Link(Link(1, Link(2)), Link(3, Link(4)))
    >>> deep_map(lambda x: x*x, nested)
    >>> nested
    Link(Link(1, Link(4)), Link(9, Link(16)))
    """
    if lst == Link.empty:
        return
    else:
        lst.first = fn(lst.first)
        deep_map(fn,lst.rest)

normal = Link(1, Link(2, Link(3)))
deep_map(lambda x: x*x, normal)
print(normal)
Link(1, Link(4, Link(9)))
