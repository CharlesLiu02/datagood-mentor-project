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
def lowest(s):
    return ((lambda y: [x for x in s if abs(x)==y])(abs(min(s, key=abs))))
print(lowest([3, -2, 2, -3, -4, 2, 3, 4]))

def plus(n):

    """Return the largest sum that results from inserting +'s into n.
    >>> plus(123456) # 12 + 34 + 56 = 102
    102
    >>> plus(1604) # 1 + 60 + 4 = 65
    65
    >>> plus(160450) # 1 + 60 + 4 + 50 = 115
    115
    """
    if n:
        return max(n%10+ plus(n//10),n%100 + plus(n//100))
    return 0
print(plus(1604)) # 12 + 34 + 56 = 102

def plusses(n, cap):
    """Return the number of plus expressions for n with values below cap.
    >>> plusses(123, 16) # 1+2+3=6 and 12+3=15, but 1+23=24 isn't below cap.
    2
    >>> plusses(2018, 38) # 2+0+1+8, 20+1+8, 2+0+18, and 2+01+8, but not 20+18.
    4
    >>> plusses(1, 2)
    1
    """
    if n < 10 and cap - n > 0:
        return 1
    elif cap <= 0:
        return 0
    else:
        return(plusses(n//10,cap-n%10)) + (plusses(n//100,cap-n%100))

print(plusses(123, 16))


class Poll:
    s = []
    def __init__(self, n):
        self.name = n
        self.votes = {}
        Poll.s.append(self)
    def vote(self, choice):
        self.votes[choice] = self.votes.get(choice, 0) + 1
def tally(c):
    """Tally all votes for a choice c as a list of (poll name, vote count) pairs.
    >>> a, b, c = Poll('A'), Poll('B'), Poll('C')
    >>> c.vote('dog')
    >>> a.vote('dog')
    >>> a.vote('cat')
    >>> b.vote('cat')
    >>> a.vote('dog')
    >>> tally('dog')
    [('A', 2), ('C', 1)]
    >>> tally('cat')
    [('A', 1), ('B', 1)]
    """
    return [(x.name, x.votes[c]) for x in Poll.s if x.votes.get(c, 0) != 0]


a, b, c = Poll('A'), Poll('B'), Poll('C')
c.vote('dog')
a.vote('dog')
a.vote('cat')
b.vote('cat')
a.vote('dog')
print(tally('dog'))
#[('A', 2), ('C', 1)]
print(tally('cat'))
#[('A', 1), ('B', 1)]

class Crooked(Poll):
    """A poll that ignores every other call to vote.
    >>> d = Crooked('D')
    >>> for s in ['dog', 'cat', 'dog', 'cat', 'cat']:
    ... d.vote(s)
    >>> d.votes
    {'dog': 2, 'cat': 1}
    """
    record = True
    def vote(self, choice):
        if self.record:
            Poll.vote(self,choice)
        self.record = not self.record




def replace(s, t, i, j):
    """Replace the slice of s from i to j with t.
    >>> s, t = Link(3, Link(4, Link(5, Link(6, Link(7))))), Link(0, Link(1, Link(2)))
    >>> replace(s, t, 2, 4)
    >>> print(s)
    <3, 4, 0, 1, 2, 7>
    >>> t.rest.first = 8
    >>> print(s)
    <3, 4, 0, 8, 2, 7>
    """
    assert s is not Link.empty and t is not Link.empty and i > 0 and i < j
    if i > 1:
        return replace(s.rest, t, i-1, j-1)
    else:
        for k in range(j - i):
            s.rest = s.rest.rest
        end = t
        while end.rest != Link.empty:
            end = end.rest
        s.rest, end.rest = t, s.rest

s, t = Link(3, Link(4, Link(5, Link(6, Link(7))))), Link(0, Link(1, Link(2)))
replace(s, t, 2, 4)



def lookups(k, key):
    """Yield one lookup function for each node of k that has the label key.
    >>> [f(v) for f in lookups(k, 2)]
    ['C', 'A']
    >>> [f(v) for f in lookups(k, 3)]
    ['S']
    >>> [f(v) for f in lookups(k, 6)]
    []
    """
    if k.label == key:
        yield lambda v: v.label
    for i in range(len(k.branches)):
        for lookup in lookups(k.branches[i],key):
            yield new_lookup(i, lookup)
def new_lookup(i, f):
    def g(v):
        return f(v.branches[i])
    return g

k = Tree(5, [Tree(7, [Tree(2)]), Tree(8, [Tree(3), Tree(4)]), Tree(5, [Tree(4), Tree(2)])])
v = Tree('Go', [Tree('C', [Tree('C')]), Tree('A', [Tree('S'), Tree(6)]), Tree('L', [Tree(1), Tree('A')])])
print([f(v) for f in lookups(k, 2)])
