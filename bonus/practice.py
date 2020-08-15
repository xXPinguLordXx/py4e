
city = (input("Enter city: "))


def get_strings (city):

    # USING WHILE LOOP:
    # index = 0
    # while index < len(city):
    #     char = city[index]
    #     return(char)
    #     index = index + 1

    # USING FOR LOOP
    # for char in city:
    #     print(char, city.count(char))

#USING DICTIONARY
    d = dict()
    for char in city:
        if char not in d:
            d[char] = 1
        else:
            d[char] = d[char] +1

    return(d)

print(get_strings(city))




#     for c in city:
#         if c == char:
#             char_count += 1
#
#     return char_count # occurences
#
# inp_word = input ("Enter word: ")
#
#
# print (get_strings)
