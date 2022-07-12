
from typing import List


def getNumberOfUniqueEmails(emails: List[str]) -> int:
    seen = set()
    for email in emails:
        temp = []
        i = 0
        while i < len(email) and email[i] != "@":
            if email[i].isalpha() or email[i].isnumeric():
                temp.append(email[i])
            i += 1
        seen.add(''.join(temp))
    return len(seen)

print(getNumberOfUniqueEmails([
    "w.......m@gmail.com", # wm
    "wa@gmail.com", # wa
    "w!#m@yahoo.com", # wm
    "jl@gmail.com", # jl
    "w_m@gmail.com", # wm
    "j.l@yahoo.com" # jl
]))