def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement  in table:
                return [i, nums.index(complement)]
            table[nums[i]] = complement