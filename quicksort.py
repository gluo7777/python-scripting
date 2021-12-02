
import math
from typing import List


def quicksort(nums: List[int]=[], low: int=0, high: int=math.inf) -> None:
    """\
    Basically merge sort but use pivot instead of middle
    """
    high = min((len(nums) if nums else 0) - 1,high)
    if low >= high:
        return
    pivot = partition(nums,low,high)
    quicksort(nums,low,pivot - 1)
    quicksort(nums,pivot + 1,high)
    

def partition(nums: List[int], low: int=0, high: int=math.inf) -> int:
    """\
    selects nums[high] as pivot

    re-arranges nums (in-place) such that elements to left of pivot are < pivot and elements right of pivot >= pivot

    returns position of pivot
    """
    high = min(len(nums) - 1,high)
    i,j = low,low
    while j < high:
        if nums[j] < nums[high]:
            swap(nums,i,j)
            i += 1
        j += 1
    swap(nums,i,high)
    return i


def swap(nums: List[int], i: int, j: int) -> None:
    temp = nums[j]
    nums[j] = nums[i]
    nums[i] = temp

def test_partition(nums: List[int]) -> None:
    print(f'Before partition: {nums}')
    partition(nums)
    print(f'After partition: {nums}')

def test_quicksort(nums: List[int]) -> None:
    print(f'Before sorting: {nums}')
    quicksort(nums)
    print(f'After sorting: {nums}')

if __name__ == "__main__":
    test_partition([9,3,5,3,6,4,1,-9,2,4])
    test_quicksort(None)
    test_quicksort([])
    test_quicksort([1])
    test_quicksort([1,2,3])
    test_quicksort([1,2,3,1])
    test_quicksort([9,4,3,1,2,8,5,7,6,0,-1,-9])
    test_quicksort([9,-3,9,-3,0,5,2,10,-5,7,6,8,4])