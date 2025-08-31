# Problem: 11. Container With Most Water

**Link:** [LeetCode - Container With Most Water](https://leetcode.com/problems/container-with-most-water/)  
**Difficulty:** Medium  

---

## 📝 Problem Statement
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`-th line are `(i, 0)` and `(i, height[i])`.  

Find two lines that together form a container, such that the container holds the **most water**.  

Return the **maximum amount of water** a container can store.  

---

## 💡 Approach

This is a **two-pointer greedy** problem:  

1. Initialize two pointers:
   - `l` at the start (`0`)  
   - `r` at the end (`n-1`)  
2. At each step:
   - Compute the area using the formula:  
     ```
     area = min(height[l], height[r]) * (r - l)
     ```
   - Update `mostWater` if this area is greater than the current maximum.  
3. Move the pointer pointing to the **shorter line**:
   - If `height[l] < height[r]`, increment `l`.  
   - Else, decrement `r`.  
4. Repeat until the pointers meet.  

This works because moving the taller line would never increase the area (width decreases and height can’t improve).  

---

## ⏱️ Complexity
- **Time:** O(n) — each pointer moves at most once across the array.  
- **Space:** O(1) — constant extra memory.  

---

## 🧑‍💻 Code

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        mostWater = 0

        while l < r:
            h = min(height[l], height[r])
            mostWater = max(mostWater, h * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return mostWater