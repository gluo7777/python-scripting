
from typing import List
from collections import Counter

def find_one(nums: List[int]) -> int:
    sum = 0
    for num in nums:
        sum = sum ^ num
    return sum

def find_one2(nums: List[int]) -> int:
    counts = Counter(nums)
    for num,count in counts.items():
        if count == 1:
            return num
    raise Exception()

print(find_one([0,1,0,2,3,2,3]))
print(find_one([10,1,10,2,1,3,4,3,4]))