class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum1=(n*(n+1))/2
        sum2=0
        for num in nums:
            sum2+=num
        return int(sum1-sum2)
