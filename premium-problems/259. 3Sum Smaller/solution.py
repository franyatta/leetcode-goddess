class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        numIndices = 0

        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < target:
                    numIndices += (k-j)
                    j += 1
                else:
                    k -=1
        
        return numIndices
            