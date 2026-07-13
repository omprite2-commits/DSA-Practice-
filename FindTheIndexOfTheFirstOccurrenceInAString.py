class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Python ka built-in find function direct index ya -1 return karta hai
        return haystack.find(needle)