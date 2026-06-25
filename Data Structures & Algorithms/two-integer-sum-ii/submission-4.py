class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        idx1 = -1
        idx2 = -1
        indexes = []
        i = 0
        j = len(numbers) - 1

        while i < j:
            current_sum = numbers[i] + numbers[j]

            if current_sum == target:
                idx1 = i + 1
                idx2 = j + 1
                break

            elif current_sum > target:
                j -= 1
            else:
                i += 1
        
        if idx1 < idx2 and idx1 != idx2:
            indexes.append(idx1)
            indexes.append(idx2)
        
        
        return indexes