if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

scores = list(arr)

for score in scores:
    max1 = max(scores)
    max2 = scores.pop(0)
    if max1 == max2:
        scores.pop(0)
    else:
        continue


print(max(scores))
