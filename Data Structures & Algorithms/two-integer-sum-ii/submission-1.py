class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        idx1 = -1
        idx2 = -1
        found = False
        indexes = []

        for first_element_idx in range(len(numbers)):
            j = first_element_idx + 1
            while j <= len(numbers) - 1:
                if numbers[j] + numbers[first_element_idx] == target:
                    idx1 = first_element_idx + 1
                    idx2 = j + 1
                    found = True
                    break
                else:
                    j += 1
            if found:
                break
        if idx1 < idx2 and idx1 != idx2:
            indexes.append(idx1)
            indexes.append(idx2)
        return indexes