fhand = open('mbox-short.txt')
count = 0

for line in fhand:
    if line.startswith('From '):
        line = line.strip()
        words = line.split()
        print(words[1])
        count += 1

print(count)
