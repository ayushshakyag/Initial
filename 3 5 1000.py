def select(k):
    return k % 3 == 0 or k % 5 ==0

n=1
answer = 0
LIMIT = 1000
while n < LIMIT:
    if select(n):
        answer += n
    n += 1

print(answer)