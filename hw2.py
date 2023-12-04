from string import punctuation

text = 'Hello world. Hello Python. Hello again.'
for c in punctuation:
    text = text.replace(c, ' ')
print(text)
result_dict = {}
for word in text.lower().split():
    if word.isalpha():
        result_dict[word] = result_dict.get(word, 0) + 1

result = [(key, value) for key, value in sorted(result_dict.items(), key=lambda x: -x[1])]
print(result[:10])
