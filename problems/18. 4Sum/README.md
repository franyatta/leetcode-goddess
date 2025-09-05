# Problem: 18. 4Sum

**Link:** [LeetCode - 4Sum](https://leetcode.com/problems/4sum/)  
**Difficulty:** Medium  

---

## 📝 Problem Statement
Given an integer array `nums` and an integer `target`, return all unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:  
0 <= a, b, c, d < n
a, b, c, d are distinct
nums[a] + nums[b] + nums[c] + nums[d] == target

The solution set must not contain duplicate quadruplets.  

---

## 💡 Approach

This is a generalization of the **2Sum / 3Sum** problems.  

### Steps:
1. **Sort the array** to simplify duplicate handling and allow two-pointer sweeps.  
2. Loop over the first element (`i`), skipping duplicates.  
3. Loop over the second element (`j`), skipping duplicates.  
4. Use **two pointers** (`l` and `r`) to find valid pairs that, together with `i` and `j`, sum to `target`.  
   - If `s == target` → record quadruplet and skip duplicates for both `l` and `r`.  
   - If `s < target` → move `l` forward to increase the sum.  
   - If `s > target` → move `r` backward to decrease the sum.  
5. Continue until all unique quadruplets are found.  

Sorting + careful duplicate skipping ensures uniqueness in the result.  

---

## ⏱️ Complexity
- **Time:** O(n³) — two nested loops (`i` and `j`) plus a two-pointer scan.  
- **Space:** O(1) extra, excluding output storage.  

---

## 🧑‍💻 Code

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        if len(nums) < 4:
            return []

        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l, r = j + 1, len(nums) - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
        return res