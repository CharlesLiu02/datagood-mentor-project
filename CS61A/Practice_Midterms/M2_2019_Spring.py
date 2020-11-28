class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ', '
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
def in_nested(v, L):
    """
    >>> in_nested(5, [1, 2, [[3], 4]])
    False
    >>> in_nested(9, [[[1], [6, 4, [5, [9]]], 7], 7, 7])
    True
    >>> in_nested(1, 1)
    True
    """
    if type(L) == int:
        return L == v
    else:
        return True in [in_nested(v,nest) for nest in L]
def link_to_dict(L):
    """
    >>> L = Link(1, Link(2, Link(3, Link(4, Link(1, Link(5))))))
    >>> print(L)
    <1, 2, 3, 4, 1, 5>
    >>> link_to_dict(L)
    {1: [2, 5], 3: [4]}
    >>> print(L)
    <1, 3, 1>
    """
    D = {}
    while L != Link.empty:
        key, value = L.first, L.rest.first
        if D.get(key,0):
            D[key] = D[key] + [value]
        else:
            D[key] = [value]
        L = L.rest.rest
    return D


def make_trie(words):
    """ Makes a tree where every node is a letter of a word.
    All words end as a leaf of the tree.
    words is given as a list of strings.
    """
    trie = Tree('')
    for word in words:
        add_word(trie, word)
    return trie

def add_word(trie, word):
    if word == '':
        return
    branch = None
    for b in trie.branches:
        if b.label == word[0]:
            branch = b
    if not branch:
        branch = Tree(word[0])
        trie.branches.append(branch)
    return add_word(branch, word[1:])

def get_words(trie):
    """
    >>> get_words(make_trie(['this', 'is', 'the', 'trie']))
    ['this', 'the', 'trie', 'is']
    """
    if trie.is_leaf():
        return [trie.label]
    return sum([[trie.label + word for word in get_words(branch)] for branch in trie.branches] , [])
print(get_words(make_trie(['this', 'is', 'the', 'trie'])))
