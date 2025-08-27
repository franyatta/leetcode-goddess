# Problem: 167. Two Sum II - Input Array Is Sorted

**Link:** [LeetCode - Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)  
**Difficulty:** Medium  

---

## 📝 Problem Statement
Given a **1-indexed** array of integers `numbers` that is sorted in **non-decreasing order**, find two numbers such that they add up to a specific `target` number.  
Return the indices of the two numbers (1-indexed) as an integer array `[index1, index2]` of length 2.  

- Each input has **exactly one solution**.  
- You **may not** use the same element twice.  

---

## 💡 Approach

Because the array is already **sorted**, we can use a **two-pointer** technique:  

1. Initialize two pointers:
   - `l` at the start (index `0`)
   - `r` at the end (index `len(numbers)-1`)  

2. Calculate the sum:
   - If `numbers[l] + numbers[r] == target` → return `[l+1, r+1]` (1-indexed).  
   - If sum is **greater** than target → move `r` left (decrease `r`).  
   - If sum is **less** than target → move `l` right (increase `l`).  

3. Continue until the correct pair is found.  

This avoids brute force (O(n²)) and leverages the sorted property for an **O(n)** solution.

---

## ⏱️ Complexity
- **Time:** O(n) — each pointer moves at most once across the array.  
- **Space:** O(1) — only a few variables are used.  

---

## 🧑‍💻 Code

```python
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