fhand = open('mbox-short.txt')
user_dict = dict()

for line in fhand:
    if line.startswith('From '):
        email = line.split()[1]
        user_dict[email] = user_dict.get(email,0) + 1


biguser = None
bigcount = None

for user,count in user_dict.items():
    if bigcount is None or count > bigcount:
        biguser = user
        bigcount = count

print(biguser, bigcount)
