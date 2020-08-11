str = input("Enter word: ")

# using while loop:
# length = len(str)
#
# while length > 0:
#     print(str[length-1])
#     length -= 1

# using for loop

for i in range(len(str), 0, -1):
    print(str[i-1])
