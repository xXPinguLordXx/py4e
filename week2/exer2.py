fhand = input("Enter filename: ")
count = 0

for line in fhand:
    if line.startswith('From '):
        line = line.strip()
        email = line.split()[1]
        print(email)
        count += 1

## use .format if there are multiple variables to display inside a string
print("There are {num} lines in file: {fname}".format(num=count, fname=fhand))



# for line in fhand:
#     if line.startswith('From '):
#         line = line.strip()
#         words = line.split()
#         print(words[1])
#         count += 1
