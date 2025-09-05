class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # bruh this problem lol

        nums.sort()

        if len(nums) < 4:
            return []

        res = []

        for i in range(len(nums)-3):
            # skip duplicates for i
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)-2):
                # skip duplicates for j
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                # two pointer sweep
                l = j + 1
                r = len(nums)-1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -=1
                        # skip duplicates for l and r
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
        return res

