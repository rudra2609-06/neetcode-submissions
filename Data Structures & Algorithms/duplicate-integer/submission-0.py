class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isDuplicate = False
        uniques = []

        for i in range(len(nums)):
            if nums[i] in uniques:
                isDuplicate = True
                break
            else:
                uniques.append(nums[i])
        return isDuplicate 
