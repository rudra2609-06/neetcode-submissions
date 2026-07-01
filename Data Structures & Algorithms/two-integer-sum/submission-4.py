class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        idx1 = -1
        idx2 = -1
        currMapper = {nums[0] : 0}

        for i in range(1,len(nums)):
            curr = nums[i]
            if currMapper.get(target - curr) != None:
                idx2 = i
                idx1 = currMapper[target - curr]
                break
            
            if curr not in currMapper:
                currMapper[curr] = i
        
        res.append(idx1)
        res.append(idx2)
        return res