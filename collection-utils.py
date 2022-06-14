import collections

lst = ['a','a','b','b','b','c']
c = collections.Counter(lst)
print(list(c))
print(dict(c))
print(set(c))

for itm,cnt in c.items():
    print(f" count of {itm} = {cnt}")