class Solution:
    def isValid(self, s: str) -> bool:
        # Brackets ko match karne ke liye ek dictionary banate hain
        # Close bracket key hoga aur Open bracket uski value
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []
        
        # String ke har ek character ko check karenge
        for char in s:
            # Agar character ek close bracket hai
            if char in mapping:
                # Stack ke top element ko nikaalein (agar stack khali nahi hai)
                # Agar stack khali hai toh koi dummy value le lein jaise '#'
                top_element = stack.pop() if stack else '#'