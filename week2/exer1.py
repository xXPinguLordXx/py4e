fhand = open('romeo.txt')
stuff = list()

for line in fhand:
    words = line.split()
    for word in words:
        if word not in stuff:
            stuff.append(word)

print(sorted(stuff))

# stuff.sort()
# print(stuff)
