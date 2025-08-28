# Problem: 238. Product of Array Except Self

**Link:** [LeetCode - Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)  
**Difficulty:** Medium  

---

## 📝 Problem Statement
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` **except** `nums[i]`.  

- You must solve it without using division.  
- The solution should run in **O(n)** time.  

---

## 💡 Approach

The key insight is to compute the product of elements **before** and **after** each index separately.  

### Steps:
1. Initialize a result array `res` with all `1`s.  
2. Traverse left to right (prefix pass):  
   - Maintain a running `prefix` product.  
   - At each index `i`, store `prefix` in `res[i]`.  
   - Update `prefix *= nums[i]`.  
3. Traverse right to left (postfix pass):  
   - Maintain a running `postfix` product.  
   - Multiply `res[i]` by `postfix`.  
   - Update `postfix *= nums[i]`.  

This way, each index accumulates the product of all numbers before and after it, without needing division.  

---

## ⏱️ Complexity
- **Time:** O(n) — two linear passes (prefix + postfix).  
- **Space:** O(1) extra (output array not counted as extra space).  

---

## 🧑‍💻 Code

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res