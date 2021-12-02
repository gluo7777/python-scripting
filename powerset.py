from typing import List

def powerset(num: int) -> List[int]:
    digits = [char for char in str(num)]
    powerset = []
    subseq = []
    for digit in digits:
        powerset.append(digit)
        subseq.append(digit)
    firstDigit = 1
    while firstDigit < len(digits):
        subseq = subseq[:len(subseq)-1]
        for i in range(0,len(subseq)):
            subseq[i] = subseq[i] + digits[firstDigit + i]
            powerset.append(subseq[i])
        firstDigit += 1
    return powerset

print(powerset(123))