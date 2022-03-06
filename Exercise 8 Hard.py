def print_word(word, number):
    word1 = word[0:number]
    word2 = word[number:len(word)]
    print(f"{word1.upper()}{word2}")


# Main Routine
enter_word = input("Enter a word: ")
enter_number = int(input("Number of characters to capitalise:"))
print_word(enter_word, enter_number)
