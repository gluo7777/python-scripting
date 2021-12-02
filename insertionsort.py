from typing import List


def insertionsort(nums: List[int]) -> None:
    if not nums or len(nums) <= 1:
        return
    for i in range(1,len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

def swap(nums: List[int], i: int, j: int) -> None:
    temp = nums[j]
    nums[j] = nums[i]
    nums[i] = temp

def test(nums: List[int]) -> None:
    print(f'Before sorting: {nums}')
    insertionsort(nums)
    print(f'After sorting: {nums}')

if __name__ == "__main__":
    test(None)
    test([])
    test([1])
    test([1,2,3])
    test([1,2,3,1])
    test([9,4,3,1,2,8,5,7,6,0,-1,-9])