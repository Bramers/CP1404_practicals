text = input("Text: ")
words = text.split(" ")
count_dict = {}
for word in words:
    count_dict[word] = count_dict.get(word, 0) + 1
length_of_longest_word = 0
for word in count_dict:
    if len(word) > length_of_longest_word:
        length_of_longest_word = len(word)
words.sort()
new_words = []
for word in words:
    if word not in new_words:
        new_words.append(word)
for word in new_words:
    print(f"{word:{length_of_longest_word}} : {count_dict[word]}")

