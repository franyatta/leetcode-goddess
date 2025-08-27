# Problem: 271. Encode and Decode Strings (Premium)

**Link:** [LeetCode - Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)  
**Difficulty:** Medium  

---

## 📝 Problem Statement
Design an algorithm to encode a list of strings to a single string, and to decode the string back to the original list.  

- You need to ensure that your encoding method is **unambiguous** (the encoded string can always be correctly decoded).  
- You may assume all strings contain only ASCII characters.  
- Implement the `encode` and `decode` methods for a `Codec` class.  

---

## 💡 Approach

The challenge is to **separate each string** in a way that avoids ambiguity (e.g., if strings contain spaces, commas, etc.).  

### Encoding Strategy
1. For each string `s`, store its **length** followed by a delimiter (`#`), then the string itself.  
   - Example: `"leet"` → `"4#leet"`.  
2. Concatenate all encoded strings into one single string.  

### Decoding Strategy
1. Traverse the encoded string while reading characters until `"#"` is found.  
2. Convert the substring before `"#"` into an integer `length`.  
3. Read the next `length` characters as the original string.  
4. Repeat until the entire encoded string is processed.  

This guarantees **no ambiguity** because the exact length of each string is explicitly stored.

---

## ⏱️ Complexity
- **Time:** O(N), where N is the total length of all strings.  
- **Space:** O(N), for building the encoded string and decoded list.  

---

## 🧑‍💻 Code

```python
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res