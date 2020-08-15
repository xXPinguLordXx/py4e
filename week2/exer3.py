numlist = list()

while True:
    number = input('Enter a number: ')
    if number == 'done':
        break

    try:
        number = float(number)
        numlist.append(number)

    except:
        print('Invalid input')
        continue

if len(numlist) == 0:
    print(None)

else:
    print('Maximum: ', max(numlist))
    print('Minimum: ', min(numlist))
