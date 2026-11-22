class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=[ch.casefold() for ch in s if ch.isalnum()]
        return cleaned==cleaned[::-1]