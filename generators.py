# Iterables store each element in Memory
def createIterable():
    mylist = [x*3 for x in range(10)]
    for x in mylist:
        print(f'Iterable={x}')

# Generators create elements on the fly and do not store
def runGenerator():
    mylist = (x*3 for x in range(10))
    for x in mylist:
        print(f'Generator={x}')

# Use yield to create instead of running a generator
# Code below does not run yet
def createGenerator():
    for x in range(10):
        yield x*3

# Code will continue executing where yield left off
def createGenerator2():
    print(0) # Do something
    yield 'Hello' # extract value
    print(5) # Do something
    yield 'World' # extract value
    print(10) # Do something
    yield '!' # extract value
    # no more lines of Code
    # generator is exhausted

createIterable()
runGenerator()

gen = createGenerator()
for i in gen:
    print(f'Yield={i}')

# Generators only run once
# No output
for i in gen:
    print(f'Yield2={i}')

for i in createGenerator2():
    print(f'Yield3={i}')
