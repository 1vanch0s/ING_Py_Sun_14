from collections import Counter    
text = open("input.txt" , "r")
if text.mode == "r":
    contents = text.read()
    
word_list = []
top_five_dai_five = []

for word in contents.split():
    clear_word = ""
    for letter in word:
        if letter.isalpha():
            clear_word += letter.lower()
    if len(clear_word) <= 3:
        continue        
    word_list.append(clear_word)
slova = Counter(word_list)
five_most_common = slova.most_common(5)
for word in five_most_common:
    top_five_dai_five.append(word[0])
the_end =sorted(top_five_dai_five)
for i in the_end:
    print(i)
