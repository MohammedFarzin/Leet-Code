def addBinary(a: str, b: str):
        sum = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1

            if j >= 0:
                carry += int(b[j])
                j -= 1

            sum.append(str(carry%2))
            carry //= 2
        return ''.join(reversed(sum)) 