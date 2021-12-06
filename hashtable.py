class HashTable:
    """
    hash by ascii sum % size
    collision by open addressing via linear probing
    load factor ?
    """

    class Item:
        def __init__(self, key: str, value: any) -> None:
            self.key = key
            self.value = value

        def __str__(self) -> str:
            return str({self.key: self.value})

    def __init__(self) -> None:
        self.__size = 10
        self.__table = [None for _ in range(self.__size)]

    def get(self, key: str) -> any:
        pos = self.hash(key)
        if self.__table[pos]:
            if self.__table[pos].key == key:
                return self.__table[pos].value
            else:  # linear probe
                i = (pos + 1) % self.__size
                while i != pos:
                    if self.__table[pos].key == key:
                        return self.__table[pos].value
                    else:
                        i = (i + 1) % self.__size
        raise KeyError(f'KeyError: {key} not found in hash table')

    def put(self, key: str, value: any) -> None:
        pos = self.hash(key)
        if self.__table[pos] == None:
            self.__table[pos] = HashTable.Item(key=key, value=value)
        elif self.__table[pos].key == key:
            self.__table[pos].value = value
        else:  # open addressing with linear probing
            i = (pos + 1) % self.__size
            while i != pos and self.__table(i):
                i = (i + 1) % self.__size
            if i != pos:
                self.__table[i] = HashTable.Item(key=key, value=value)
            else:
                raise Exception(
                    'Hash table is full and resizing not implemented')

    def hash(self, key: str) -> int:
        if not key or len(key) == 0:
            raise KeyError('Cannot hash empty key')
        keysum = 0
        for i in range(len(key)):
            char = key[i]
            keysum += ord(char) * (i + 1)
        return keysum % self.__size

    def print(self) -> None:
        for pos in range(self.__size):
            item = self.__table[pos]
            if item:
                print(f'pos={pos}, item={item}')


if __name__ == '__main__':
    ht = HashTable()
    ht.put('William', 'developer')
    print(ht.get('William'))
    ht.put('Kat', 'girlfriend')
    ht.put('Kat', 'wife')
    ht.put('Sam', 'dog')
    ht.print()
