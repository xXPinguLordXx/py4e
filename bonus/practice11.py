word = input("Enter word here: ")
char = input("Enter character here: ")


def count (word, char):
    char_count = 0
    for letter in word:
        if letter == char:
            char_count = char_count + 1
    print(char_count)


count(word, char)
