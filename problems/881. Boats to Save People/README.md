# Problem: 881. Boats to Save People

**Link:** [LeetCode - Boats to Save People](https://leetcode.com/problems/boats-to-save-people/)  
**Difficulty:** Medium  

---

## 📝 Problem Statement
You are given an array `people` where `people[i]` is the weight of the `i`-th person, and an integer `limit` representing the maximum weight a boat can carry.  

Each boat can carry at most **two people** at the same time, provided their combined weight does not exceed `limit`.  

Return the **minimum number of boats** required to carry every person.  

---

## 💡 Approach

This is a **greedy two-pointer** problem:  

1. Sort `people` in non-decreasing order.  
2. Use two pointers:
   - `i` at the lightest person.  
   - `j` at the heaviest person.  
3. At each step:
   - If the lightest (`people[i]`) + heaviest (`people[j]`) can fit in one boat → put them together and move both pointers.  
   - Otherwise → the heaviest person goes alone, move `j` only.  
4. Count a boat each iteration until all people are assigned.  

This greedy approach works because pairing the lightest with the heaviest always optimizes space.  

---

## ⏱️ Complexity
- **Time:** O(n log n) — sorting dominates the runtime.  
- **Space:** O(1) — only pointers and counters are used.  

---

## 🧑‍💻 Code

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()

        i = 0
        j = len(people) - 1

        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            boats += 1

        return boats