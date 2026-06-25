class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       
        res = []
        nums = sorted(nums)

        for i in range(len(nums)):
            if nums[i] == nums[i - 1] and i > 0:
                continue 
            j = i + 1
            k = len(nums) - 1
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]

                # if current_sum < 0(target)
                if current_sum < 0:
                    j += 1
                # if current_sum > 0(target)
                elif current_sum > 0:
                    k -= 1
                # if current_sum == 0(target)
                elif current_sum == 0:
                    if i != j and j != k and k != i:
                        triplet = []
                        triplet.append(nums[i])
                        triplet.append(nums[j])
                        triplet.append(nums[k])
                        if triplet not in res:
                            res.append(triplet)
                        j += 1
                        k -= 1
        return res




        