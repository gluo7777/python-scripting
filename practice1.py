# determine if number is a palindrome
## whole number
## 0 == true
## 10 == false
## 101 == true
## -101 <> 101-
## 1010 <> 0101

def is_palindrome(num: int) -> bool:
    num = str(num)
    s = [ num[i] for i in range(len(num) - 1,-1,-1) ]
    for i in range(len(num)):
        if num[i] != s[i]:
            return False
    return True

# print(is_palindrome(101))
# print(is_palindrome(10))
# print(is_palindrome(-10))
# print(is_palindrome(-101))

def is_palindrome2(num: int) -> bool:
    if num < 0:
        return False
    a = []
    while num > 0:
        a.append(num % 10)
        num = int(num / 10)
    x,y = 0,len(a) - 1
    while x < y:
        if a[x] != a[y]:
            return False
        x += 1
        y -= 1
    return True

assert is_palindrome2(101)
assert not is_palindrome2(1010)
assert not is_palindrome2(10)
assert not is_palindrome2(-10)
assert not is_palindrome2(-101)