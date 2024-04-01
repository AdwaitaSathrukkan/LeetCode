import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum=0
        max_sum=sys.maxsize-1 
        for i in range(len(nums)):
            cur_sum+=nums[i]
            if cur_sum>max_sum:
                max_sum=cur_sum
            if cur_sum<0:
                cur_sum=0
        return max_sum
    
# Time complexity: O(n)
# Space complexity: O(1)
# The above code is an implementation of Kadane's algorithm.
#dp