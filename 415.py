class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        digit_map = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
        }
        
        char_map = "0123456789"
        
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []
        
        while i >= 0 or j >= 0 or carry:
            d1 = digit_map[num1[i]] if i >= 0 else 0
            d2 = digit_map[num2[j]] if j >= 0 else 0
            
            total = d1 + d2 + carry
            carry = total // 10
            result.append(char_map[total % 10])
            
            i -= 1
            j -= 1
            
        return "".join(result[::-1])
