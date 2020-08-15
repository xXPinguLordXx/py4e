fhand = open('romeo.txt')
stuff = list()

for line in fhand:
    line2 = line.split()
    for word in line2:
        if word not in stuff:
            stuff.append(word)

stuff.sort()
print(stuff)
