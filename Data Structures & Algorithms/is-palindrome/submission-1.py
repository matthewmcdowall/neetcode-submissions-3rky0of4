import string

class Solution:
    def isPalindrome(self, s: str) -> bool:


        table = str.maketrans('','',string.punctuation)
        s = s.translate(table)
        s = s.replace(" ", "")

        i = 0
        j = len(s) - 1

        while i < j: #i cant be greater than j or we have cross or p1 over p2

            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j -=1
        return True

        
        