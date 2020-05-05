class Person(object):
    """docstring for Person."""
    def __init__(self, first, last):
        super(Person, self).__init__()
        self.first = first
        self.last = last

    def tostring(self):
        print(f'Hi, this is {will.first} {will.last}')

will = Person('Wiliam','Luo')
will.tostring()
