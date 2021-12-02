# array

'''
arrays in python:
- implemented as variable length arrays
'''

array = [1,2,3]
assert len(array) == 3
assert array[0] == 1
assert array[1:2] == [2]
assert array[1:len(array)] == [2,3]
old_addr = hex(id(array))
array.append(4)
new_addr = hex(id(array))
assert old_addr == new_addr # modifications to array modifies same object in memory
assert array[-1] == 4
array.insert(1,-2)
assert array[1] == -2
assert array[2] == 2
array = [1,2,3]
array.remove(2)
assert array == [1,3]
array = [1,2,3]
array.reverse()
assert array == [3,2,1]

# string

'''
strings are immutable
modification of a string -> creates a new string
'''
str1 = 'Hi, Let us learn strings in Python'
str1_addr = hex(id(str1))
str2 = str1 + '.'
str2_addr = hex(id(str2))
assert str1_addr != str2_addr
assert str1[0:2] == 'Hi'
assert str1[-6:] == 'Python'
str2 = 'abc'
strarray = [c for c in str2]
strarray.sort(reverse=True)
assert strarray == ['c','b','a']

# linked lists

'''
singly linked list
'''

class ListNode:
    def __init__(self, val:int=0, next:'ListNode'=None) -> None:
        self.val = val
        self.next = next

array = [1,2,3]
prevNode = None
headNode = None
for v in array:
    node = ListNode(v)
    if prevNode:
        prevNode.next = node
    if not headNode:
        headNode = node
    prevNode = node
curNode = headNode
nodeArray = []
while curNode:
    nodeArray.append(curNode.val)
    curNode = curNode.next
assert nodeArray == array

'''
double linked list
- singly linked list can be converted to this by adding pointer to prev node
'''
prevNode = None
curNode = headNode
while curNode:
    curNode.prev = prevNode
    prevNode = curNode
    curNode = curNode.next
lastNode = prevNode
nodeArray = []
while lastNode:
    nodeArray.append(lastNode.val)
    lastNode = lastNode.prev
assert nodeArray == sorted(array,reverse=True)

# queue

'''
implement using Deque and not list
'''

from typing import Deque, List
queue = Deque()
## enqueue
queue.append(1)
queue.append(2)
queue.append(3)
## peek
assert queue[0] == 1
## dequeue
assert queue.popleft() == 1
assert list(queue) == [2,3]

# stack

'''
list has stack operations
'''

stack = []
## push
stack.append(1)
stack.append(2)
stack.append(3)
## peek
assert stack[-1] == 3
## pop
assert stack.pop() == 3
assert stack == [1,2]

'''
recursion also creates a stack implicitly
'''

def func(val: int=0):
    print(f'entering func({val})')
    if val > 0:
        func(val - 1)
    print(f'exiting func({val})')
func(10)

'''
hash table
 - python dicts are hash tables
'''

ht = {}
ht['dog'] = 'will'
ht['cat'] = 'bob'
assert 'dog' in ht
assert 'cat' in ht
assert sorted(ht.keys()) == ['cat','dog']
assert sorted(ht.values()) == ['bob','will']
for k,v in ht.items():
    print(f'{k}={v}')

'''
custom hash function implements __hash__() method
'''

class Student:
    def __init__(self, id:int, name:str) -> None:
        self.id = id
        self.name = name
    
    def __hash__(self) -> int:
        return self.id.__hash__()

s1,s2,s3 = Student(id=1,name='Will'),Student(id=2,name='Dave'),Student(id=3,name='Charlot')

ht = {}
ht[s1] = s1.name
ht[s2] = s2.name
ht[s3] = s3.name
assert ht[s2] == s2.name

# set
set1 = set()
set1.add('will')
set1.add('dave')
set1.add('will')
set1.add('will')
assert len(set1) == 2

# tree

class TreeNode:
    def __init__(self, val:int=0, children:List['TreeNode']=[]) -> None:
        self.val = val
        self.children = children

