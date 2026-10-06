class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Turn list to hashtable
        nums_hash = {}
        for idx, num in enumerate(nums):
            comp = target - num
            if comp in nums_hash:
                return [nums_hash[comp], idx]
            nums_hash[num] = idx