class Solution:
    def reverse(self, x: int) -> int:
        maxi = 2**31 - 1
        mini = -2**31
        rev = 0
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)

        while x:
            digit = x % 10
            rev = rev*10 + digit
            x = x // 10
        rev *= sign
        if rev < mini or rev > maxi:
            return 0
        else:
            return rev

        