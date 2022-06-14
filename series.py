sum = 0
for i in range(1,101,1):
    sum += i
    if sum >= 3600:
        print(i)
        break
# print(sum)