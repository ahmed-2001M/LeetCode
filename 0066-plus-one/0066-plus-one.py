class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        for i in range(len(digits)-1,-1,-1):
            res = digits[i]+carry
            digits[i] = (res)%10
            carry = res//10
        if carry:
            return [carry]+digits
            
        return digits