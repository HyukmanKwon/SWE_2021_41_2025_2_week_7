from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i, j]
            
nums1 = [2, 7, 11, 15]
target1 = 9
print(f"입력: nums = {nums1}, target = {target1}")
print(f"예상 출력: [0, 1]")
print(f"실행 결과: {twoSum(nums1, target1)}")
print("-" * 20)
# 예제 2
nums2 = [3, 2, 4]
target2 = 6
print(f"입력: nums = {nums2}, target = {target2}")
print(f"예상 출력: [1, 2]")
print(f"실행 결과: {twoSum(nums2, target2)}")
print("-" * 20)

# 예제 3
nums3 = [3, 3]
target3 = 6
print(f"입력: nums = {nums3}, target = {target3}")
print(f"예상 출력: [0, 1]")
print(f"실행 결과: {twoSum(nums3, target3)}")