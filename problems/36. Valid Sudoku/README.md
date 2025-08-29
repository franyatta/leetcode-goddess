# Problem: 36. Valid Sudoku

**Link:** [LeetCode - Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)  
**Difficulty:** Medium  

---

## 📝 Problem Statement
Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:  

1. Each row must contain the digits `1-9` without repetition.  
2. Each column must contain the digits `1-9` without repetition.  
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.  

Note:  
- A Sudoku board (partially filled) could be valid but not necessarily solvable.  
- Only the filled cells (non `"."`) need to be checked.  

---

## 💡 Approach

To efficiently validate the board, we use **hash sets** to track the digits we’ve seen in:  

- Each row  
- Each column  
- Each `3x3` square (identified by `(r // 3, c // 3)` coordinates)  

### Steps:
1. Loop through every cell `(r, c)` in the board.  
2. Skip if the cell is `"."`.  
3. Check if the digit is already in the current row, column, or square’s set:  
   - If yes → invalid Sudoku → return `False`.  
   - If no → add it to the corresponding sets.  
4. If no conflicts are found → return `True`.  

This ensures all Sudoku rules are respected in **one pass**.  

---

## ⏱️ Complexity
- **Time:** O(81) → effectively O(1), since the board size is fixed at `9x9`.  
- **Space:** O(81) → up to 27 sets (9 rows + 9 columns + 9 squares).  

---

## 🧑‍💻 Code

```python
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)  # keys: (r//3, c//3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True