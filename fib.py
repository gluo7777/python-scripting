

def fib_bottom_up(n: int) -> int:
    if n == 0:
        return 0
    i = 2
    x,y = 0,1
    while i <= n:
        t = y
        y = x + y
        x = t
        i += 1
    return y

for n in range(20):
    print(f'fib({n}) = {fib_bottom_up(n)}')