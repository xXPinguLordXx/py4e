def count (word, char):
    char_count = 0

    for c in word:
        if c == char:
            char_count += 1

    return char_count # occurences

inp_word = input ("Enter word: ")
inp_char = input ("Enter char: ")


print (count)
