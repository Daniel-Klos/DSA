class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        count = Counter(nums)
        for num in nums:
            if count[num] > 1:
                return True

        return False