class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()

        leftPointer = 0
        rightPointer = len(s) - 1
        isPalindrome = True
        while leftPointer < rightPointer:
            if not s[leftPointer].isalnum():
                leftPointer += 1
            elif not s[rightPointer].isalnum():
                rightPointer -= 1
            elif s[leftPointer] == s[rightPointer]:
                leftPointer += 1
                rightPointer -= 1
            else:
                isPalindrome = False
                break


            
        
        return isPalindrome

        
        