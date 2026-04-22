class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i_index = 0
        for i in nums:
            j_index = 0
            for j in nums:
                if target - i == j:
                    if i_index == j_index:
                        j_index += 1
                    elif i_index > j_index:
                        return [j_index, i_index]
                    else:
                        return [i_index, j_index]
                else:
                    j_index += 1
            i_index += 1
                    