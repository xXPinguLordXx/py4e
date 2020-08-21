numlist = list()

while True:
    number = input('Enter a number: ')
    if number == 'done':
        break

    try:
        number = float(number)


    except:
        print('Invalid input')
        continue

    numlist.append(number)

if len(numlist) == 0:
    print(None)

else:
    print('Maximum: ', max(numlist))
    print('Minimum: ', min(numlist))
