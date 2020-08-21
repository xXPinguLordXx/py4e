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


def middle (numlist):
    return numlist[1:-1]

print(middle(numlist))
