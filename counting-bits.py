from typing import List
import math

def counting_bits(n) -> List[int]:
    if n == 0:
        return [0]

    dp = [0] * (n + 1)

    e = -1
    for x in range(1,n+1):
        if math.pow(2,e + 1) == x:
            e += 1
        offset = int(math.pow(2,e))
        dp[x] = 1 + dp[x - offset]
    return dp

for x in range(64):
    print(f'{x} : {counting_bits(x)}')