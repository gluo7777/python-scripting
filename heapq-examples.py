# https://docs.python.org/3/library/heapq.html

from heapq import heappush, heappop

# Min Heap
minheap = []
heappush(minheap, 10)
heappush(minheap, 5)
heappush(minheap, 1)
heappush(minheap, 3)
heappush(minheap, 2)
heappush(minheap, -5)
assert len(minheap) == 6
assert minheap[0] == -5
heappop(minheap)
assert minheap[0] == 1
heappop(minheap)
assert minheap[0] == 2
assert len(minheap) == 4

# Max Heap
maxheappush = lambda array,x : heappush(array, x * -1)
maxheappop = lambda array : heappop(array) * -1
maxheap = []
maxheappush(maxheap, 10)
maxheappush(maxheap, 5)
maxheappush(maxheap, 1)
maxheappush(maxheap, 3)
maxheappush(maxheap, 2)
maxheappush(maxheap, -5)
assert len(maxheap) == 6
assert maxheappop(maxheap) == 10
assert maxheappop(maxheap) == 5
assert maxheappop(maxheap) == 3
assert len(maxheap) == 3

# heap with tuples

h = []
hpush = lambda w,f : heappush(h, (f * -1,w))
hpop = lambda : heappop(h)[1]

hpush("task1",10)
hpush("task2",20)
hpush("task3",5)
assert hpop() == "task2"
assert hpop() == "task1"
assert hpop() == "task3"