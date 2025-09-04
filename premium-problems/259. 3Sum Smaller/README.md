# Problem: 259. 3Sum Smaller (Premium)

**Link:** [LeetCode - 3Sum Smaller](https://leetcode.com/problems/3sum-smaller/)  
**Difficulty:** Medium  

---

## 📝 Problem Statement
Given an integer array `nums` and an integer `target`, return the **number of index triplets** `(i, j, k)` with `0 <= i < j < k < n` such that:  nums[i] + nums[j] + nums[k] < target

---

## 💡 Approach

This is a variation of the classic **3Sum** problem, but instead of finding exact matches, we count all triplets whose sum is **less than** the target.  

### Steps:
1. **Sort the array** to allow the use of two-pointer technique.  
2. Fix one number at index `i`.  
3. Use two pointers:
   - `j = i + 1` (just after `i`)  
   - `k = len(nums) - 1` (end of array)  
4. Calculate `s = nums[i] + nums[j] + nums[k]`.  
   - If `s < target`, then all elements from `j` through `k` with `nums[i]` form valid triplets.  
     - Count them as `(k - j)` and move `j` forward.  
   - Otherwise, move `k` leftward to reduce the sum.  
5. Continue until all valid triplets are counted.  

This leverages sorting + two pointers to avoid O(n³) brute force.  

---

## ⏱️ Complexity
- **Time:** O(n²) — sorting O(n log n), plus nested two-pointer loops.  
- **Space:** O(1) — in-place, ignoring sort.  

---

## 🧑‍💻 Code

```python
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        numIndices = 0

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < target:
                    numIndices += (k - j)
                    j += 1
                else:
                    k -= 1
        return numIndices