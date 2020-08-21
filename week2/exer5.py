fhand = open('mbox-short.txt')
days = dict()

for line in fhand:
    if line.startswith('From '):
        day = line.split()[2]
        days[day] = days.get(day,0) + 1

print(days)

#Kuya Paul's longer code:
#
# for line in fhand:
#     if line.startswith('From '):
#         day = line.split()[2]
#         if day in days.keys():
#             days[day] = days[day] + 1 #or days[day] += 1
#         else:
#             days[day]
