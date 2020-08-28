if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

scores = list(arr)
max1  = max(scores)
max2 = -101

for score in scores:
    if max2 < score < max1:
        max2 = score

if max2 == -101:
    max2 = None
print(max2)
