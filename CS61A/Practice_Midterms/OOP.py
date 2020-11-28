class CircularBuffer:
    """Doctests:

    >>> buffer = CircularBuffer(3)
    >>> buffer.remove()
    Buffer is empty
    >>> buffer.append('a')
    >>> buffer.remove()
    'a'
    >>> buffer.remove()
    Buffer is empty
    >>> buffer.append('b')
    >>> buffer.append('c')
    >>> buffer.append('d')
    >>> buffer.append('e')
    Buffer capacity exceeded
    >>> buffer.remove()
    'b'
    >>> buffer.remove()
    'c'
    >>> buffer.remove()
    'd'
    >>> buffer.remove()
    Buffer is empty
    """
    def __init__(self, n):
        self.array = [None]*n   # list of length n
        self.n = n
        self.start = 0
        self.end = 0

    def append(self, elem):
        if self.end <= self.n-1:
            self.array[self.end] = elem
            self.end += 1
        else:
            print('Buffer capacity exceeded')

    def remove(self):
        if self.array[0] == None:
            print('Buffer is empty')
        else:
            x = self.array.pop(0)
            self.array.append(None)
            self.end -=1
            print(x)



class Chef:
    """Doctests:

    >>> albert = Chef('quiche', ['egg', 'cheese', 'cream', 'salt'])
    >>> ramsay = Chef('steak', ['meat', 'bbq sauce', 'salt'])
    >>> ramsay.cook()
    'Not enogh ingredients!'
    >>> ramsay.serve()
    'No food to serve!'
    >>> ramsay.fetch_ingredients()     # 1 salt remaining
    "Fetched: ['meat', 'bbq sauce', 'salt']"
    >>> ramsay.cook()
    'Cooked steak!'
    >>> ramsay.serve()
    >>> Chef.finished
    ['steak']
    >>> albert.fetch_ingredients()     # 0 salt remaining
    "Fetched: ['egg', 'cheese', 'cream', 'salt']"
    >>> albert.cook()
    'Cooked quiche!'
    >>> albert.serve()
    >>> Chef.finished
    ['steak', 'quiche']
    >>> ramsay.fetch_ingredients()
    'No more salt!'
    """
    ingredients = [ ]
    finished = [ ]
    def __init__(self,food, recipe):
        self.food = food
        self.recipe = recipe
        for food in self.recipe:
            if food not in self.ingredients:
                self.ingredients.append(food)
                self.ingredients.append(food)
        self.ready = False
        self.cooked = False
        self.fetched = False
    def fetch_ingredients(self):
        for food in self.recipe:
            if food in self.ingredients:
                self.ingredients.remove(food)
            else:
                return 'No more ' +  food + '!'
        self.fetched = True
        return 'Fetched: ' + str(self.recipe)
    def cook(self):
        if not self.fetched:
            return 'Not enough ingredients!'
        else:
            self.cooked = True
            self.fetched = False
            return 'Cooked ' + self.food
    def serve(self):
        if not self.cooked:
            return 'No food to serve!'
        else:
            self.cooked = False
            self.finished.append(self.food)
albert = Chef('quiche', ['egg', 'cheese', 'cream', 'salt'])
ramsay = Chef('steak', ['meat', 'bbq sauce', 'salt'])
print(ramsay.cook())
ramsay.serve()
ramsay.fetch_ingredients()     # 1 salt remaining
ramsay.cook()
ramsay.serve()
Chef.finished
albert.fetch_ingredients()     # 0 salt remaining
albert.cook()
albert.serve()
Chef.finished
ramsay.fetch_ingredients()
