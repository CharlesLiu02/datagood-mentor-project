
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
def quota(f, limit):
    """A decorator that limits the number of times a value can be returned.
    >>> square = lambda x: x * x
    >>> square = quota(square, 3)
    >>> square(6) # 1st call with return value 36
    36
    >>> [square(5) for x in range(3)] # 3 calls when the limit is 3
    [25, 25, 25]
    >>> square(5) # 4th call with return value 25
    'Over quota! Limit is now 2'
    >>> square(-6) # 2nd call with return value 36
    36
    >>> square(-6) # 3rd call when the limit is 2
    'Over quota! Limit is now 1'
    >>> square(7) # 1st call when the limit is 1
    49
    >>> square(5) # 5th call with return value 25
    'Over quota! Limit is now 0'
    """
    values = []
    def limited(n):
        nonlocal limit
        y = f(n)
        count = len([x for x in values if x == f(n)])
        values.append(y)
        if count < limit:
            return y
        limit = limit - 1
        return 'Over quota! Limit is now ' + str(limit)
    return limited

class VotingMachine:
    """A machine that creates and records ballots.
    >>> machine = VotingMachine(4)
    >>> a, b, c, d = machine.ballots
    >>> d.vote('Bruin')
    'Bruin is winning'
    >>> b.vote('Bruin')
    'Bruin is winning'
    >>> c.vote('Bear')
    'Bear is losing'
    >>> a.vote('Bear')
    'Bear is winning'
    >>> c.vote('Tree')
    'Fraud: multiple votes from the same ballot!'
    >>> machine.winner
    'Bear'
    """
    def __init__(self, k):
        self.ballots = [Ballot(self) for i in range(k)]
        self.votes = {}
    def record(self, ballot, choice):
        if ballot.used:
            return 'Fraud: multiple votes from the same ballot!'
        ballot.used = True
        self.votes[choice] = self.votes.get(choice , 0) + 1
        if self.votes[choice] < max([self.votes[key] for key in self.votes]) :
            return choice + ' is losing'
        else:
            self.winner = choice
            return choice + ' is winning'
class Ballot:
    used = False
    def __init__(self, machine):
        self.machine = machine
    def vote(self, x):
        return VotingMachine.record(self.machine, self, x)

def path(s, t):
    """Return whether Link S is a path from the root to a leaf in Tree T.
    >>> t = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6)])
    >>> a = Link(1, Link(3, Link(4))) # A full path
    >>> path(a, t)
    True
    >>> b = Link(1, Link(3)) # A partial path
    >>> path(b, t)
    False
    >>> c = Link(1, Link(2, Link(7))) # A path and an extra value
    >>> path(c, t)
    False
    >>> d = Link(3, Link(4)) # A path of a branch
    >>> path(d, t)
    False
    """
    if s == Link.empty and t.label:
        return False
    if s.first == t.label and t.is_leaf() and s.rest == Link.empty :
        return True
    return any([path(s.rest, b) for b in t.branches])

def binary(s):
    """Construct a binary search tree from S for which all paths are in order.
    >>> binary([3, 5, 1])
    BTree(3, BTree(1), BTree(5))
    >>> binary([4, 3, 7, 6, 2, 9, 8])
    BTree(4, BTree(3, BTree(2)), BTree(7, BTree(6), BTree(9, BTree(8))))
    """
    assert len(s) == len(set(s)), 'All elements of s should be unique'
    if ________________________________________________________________________:
        return ________________________________________________________________
    root = ____________________________________________________________________
    left = ____________________________________________________________________
    right = ___________________________________________________________________
    return BTree(root, binary(left), binary(right))

def sums(n, k):
    """Return the ways in which K positive integers can sum to N.
    >>> sums(2, 2)
    [[1, 1]]
    >>> sums(2, 3)
    []
    >>> sums(4, 2)
    [[3, 1], [2, 2], [1, 3]]
    >>> sums(5, 3)
    [[3, 1, 1], [2, 2, 1], [1, 3, 1], [2, 1, 2], [1, 2, 2], [1, 1, 3]]
    """
    if k == 1:
        return [[n]]
    y = []
    for x in range(1,n):
        y.extend([s + [x] for s in sums(n-x,k-1)])
    return y


f = lambda x, y: (x and [[x] + z for z in y] + f(x-1, y)) or []
def sums(n, k):
    """Return the ways in which K positive integers can sum to N."""
    g = lambda w: (w and f(n,g(w-1))) or [[]]
    return [v for v in g(k) if sum(v) == n]
print(sums(5,3))
