class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Voting Algorithm
        count = 0
        candidate = 0

        for num in nums:
            if count==0:
                candidate = num

            if num==candidate:
                count+=1
            else:
                count -=1
        return candidate
        
# class Solution:
#     #brute force
#     def majorityElement(self, nums: List[int]) -> int:
#         n = len(nums)
#         for i in range(n):
#             if nums.count(nums[i])>int(n/2):
#                 return nums[i]
        