def longest_word(word_list):
    longest = ""
    for word in word_list:
        if len(word) > len(longest):
            longest = word
    return longest


# Main Routine
words= []
word_ = ""
while word_ != "1":
    word_ = input("Add word to list ( or 1 to end): ")
    words.append(word_)
print(longest_word(words))
