class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Turn list to hashtable
        nums_hash = {}
        for idx, num in enumerate(nums):
            if num not in nums_hash:
                nums_hash[num] = []
            nums_hash[num].append(idx)

        for e in nums_hash.keys():
            comp = target - e
            if comp in nums_hash.keys():
                if e == comp:
                    if len(nums_hash[e]) == 2:
                        return [nums_hash[e][0], nums_hash[e][1]]
                    else:
                        continue
                return [nums_hash[e][0], nums_hash[comp][0]]                