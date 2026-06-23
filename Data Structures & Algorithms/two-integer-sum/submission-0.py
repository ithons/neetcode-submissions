class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j_value = target - nums[i]
            if j_value == nums[i] and nums.count(j_value) < 2: continue
            if j_value in nums:
                j = nums.index(j_value, i+1)
                return [i, j]