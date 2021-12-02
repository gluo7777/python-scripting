from typing import List


def insertionsort(nums: List[int]) -> None:
    for i in range(0,len(nums) if nums else 0):
        for j in range(0,i):
            if nums[i] <= nums[j]:
                swap(nums,i,j)
                for k in range(j + 1,i):
                    swap(nums,i,k)
                break

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