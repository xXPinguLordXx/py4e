def every_three_nums(start):
    lst = list()

    for i in range(start, 101, 3):
        lst.append(i)

    return lst

start = int(input())
print(every_three_nums(start))
