from typing import List
import math

def mergesort(nums: List[int], left: int=0, right: int=math.inf) -> None:
    right = min(right,len(nums))
    if left >= right:
        return
    middle = left + int((right - left) / 2)
    mergesort(nums,left,middle)
    mergesort(nums,middle + 1,right)
    merge(nums,left,middle,right)

def merge(nums: List[int], left: int, middle: int, right: int) -> None:
    leftNums = nums[left:middle + 1]
    rightNums = nums[middle + 1:right + 1]
    x,leftStart,rightStart,leftEnd,rightEnd = left,0,0,len(leftNums),len(rightNums)
    while leftStart < leftEnd and rightStart < rightEnd:
        if leftNums[leftStart] <= rightNums[rightStart]:
            nums[x] = leftNums[leftStart]
            leftStart += 1
        else:
            nums[x] = rightNums[rightStart]
            rightStart += 1
        x += 1
    while leftStart < leftEnd:
        nums[x] = leftNums[leftStart]
        x,leftStart = x + 1,leftStart + 1
    while rightStart < rightEnd:
        nums[x] = rightNums[rightStart]
        x,rightStart = x + 1,rightStart + 1

def test(nums: List[int]) -> None:
    print(f'Before sorting: {nums}')
    mergesort(nums)
    print(f'After sorting: {nums}')

if __name__ == "__main__":
    test([])
    test([1])
    test([1,2,3])
    test([1,2,3,1])
    test([9,4,3,1,2,8,5,7,6,0,-1,-9])