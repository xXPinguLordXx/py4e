#declare this shit outside the loop because if you put it inside it will just get looped forever
#declare this outside so that it is accessible by the entire program outside and not just within the loop
sum = 0
count = 0
max = None
min = None

while True:
    number = input ("Enter a number: ")
    if number == 'done':
        break

    try:
        number = float(number)

    except:
        print('Invalid input')
        continue

    sum += number #this is shorthand for sum = sum + number
    count = count + 1 #or you can write count += 1 #write this here so that program tries to do this before moving on to invalidating

    if max is None:
        max = number
    elif max < number:
        max = number

    if min is None:
        min = number
    elif min > number:
        min = number

print(sum, count, min, max)
