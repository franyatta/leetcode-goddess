class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers)-1

        for i in range(len(numbers)):
            tot = numbers[r] + numbers[l]
            if tot > target:
                r -= 1
            elif tot < target:
                l += 1
            elif tot == target:
                return [l+1, r+1]
            else:
                return [-1, -1]