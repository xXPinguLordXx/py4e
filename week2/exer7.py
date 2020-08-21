fhand = open('mbox-short.txt')
user_dict = dict()

for line in fhand:
    if line.startswith('From '):
        email = line.split()[1].split('@')[1]
        user_dict[email] = user_dict.get(email,0) + 1




print(user_dict)
