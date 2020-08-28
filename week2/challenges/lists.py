if __name__ == '__main__':
    N = int(input())

numlist = list()

for i in range(N):
    cmd = str(input())
    if 'insert' in cmd:
        numlist.insert(int(cmd.split()[1]),int(cmd.split()[2]))

    elif cmd == 'print':
        print(numlist)

    elif 'remove' in cmd:
        numlist.remove(int(cmd.split()[1]))

    elif 'append' in cmd:
        numlist.append(int(cmd.split()[1]))

    elif cmd == 'sort':
        numlist.sort()

    elif cmd == 'pop':
        del numlist[-1]

    elif cmd == 'reverse':
        numlist.reverse()
