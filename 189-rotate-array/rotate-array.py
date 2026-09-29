class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        
        copy = [0] * len(nums)
        for i in range(k, len(nums)):
            copy[i] = nums[i-k]

        for i in range(0, k):
            copy[k - i - 1] = nums[len(nums) - 1 - i]

        for i in range(len(nums)):
            nums[i] = copy[i]