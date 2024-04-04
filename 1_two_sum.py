class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _hash = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in _hash:
                return [_hash[complement], i]  # Return as soon as the pair is found
            _hash[num] = i  # Store index of `num` after checking for its complement
