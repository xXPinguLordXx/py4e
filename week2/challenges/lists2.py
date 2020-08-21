numlist = ['1','2','3']

cmd = str(input())


if 'insert' in cmd:
    i = int(cmd.split()[1])
    e = int(cmd.split()[2])
    numlist.insert(e,i)
    print(numlist)
