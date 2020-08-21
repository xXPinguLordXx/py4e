if __name__ == '__main__':
    N = int(input())

numlist = list()
cmd = str(input())


# COMMANDS
    if 'insert' in cmd:
        i = int(cmd.split()[1])
        e = int(cmd.split()[2])
        numlist.insert(e,i)
        print(numlist)
    elif cmd == 'print':
        print(numlist)

    elif cmd == 'sort':
        numlist.sorted()
    elif cmd == 'pop':
        del numlist[-1]
    elif cmd == 'reverse':
        numlist.reverse()
