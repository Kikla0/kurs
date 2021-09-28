text = input()

text = text.lower()

for character in [' ', ',', '.']:
    if character in text:
        text = text.replace(character, '')

dictionary = {}

for letter in text:
    if letter in dictionary:
        dictionary[letter] += 1
    else:
        dictionary[letter] = 1

print(dict(sorted(dictionary.items())))