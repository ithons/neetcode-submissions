class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        unique_nums = set(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                n3 = -(nums[i]+nums[j])
                if n3 in unique_nums:
                    index = nums.index(n3)
                    if index!=i and index!=j:
                        triplets.add(tuple(sorted([nums[i],nums[j],nums[index]])))
        return [list(tup) for tup in triplets]
