fhand = open('romeo.txt')

stanza = fhand.read()
print(stanza)

for line in stanza:
    word = line.split()
    print(word)
