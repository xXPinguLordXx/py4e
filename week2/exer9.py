fhand = open('mbox-short.txt')
hours = dict()

for line in fhand:
    if line.startswith('From '):
        hour = line.split()[5].split(':')[0]
        hours[hour] = hours.get(hour,0) + 1

hours_list = []
for k,v in hours.items():
    hours_list.append((k,v))

for k,v in sorted(hours_list):
    print(k,v)


## OR

# [print(k,v) for k,v in sorted([(k,v) for k,v in hours.items()])]
