numlist = list()

while True:
    number = input('Enter a number: ')
    if number == 'done':
        break

    try:
        number = int(number)
        numlist.append(number)

    except:
        print('Invalid input')
        continue


def chop (numlist):
    del numlist[0]
    del numlist[-1]
    return None


def middle (numlist):
    del numlist[0]
    del numlist[-1]
    newlist = numlist
    return newlist

if len(numlist) == 0 or 1:
    print('Needs more data pls')
else:
    print(middle(numlist))
