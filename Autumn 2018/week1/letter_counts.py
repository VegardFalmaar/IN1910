def count_chars(str):
    dict = {}
    for letter in str.lower():
        if letter not in dict:
            dict[letter] = 1
        else:
            dict[letter] += 1
    return dict

example = "Hello, world!"
for char, count in sorted(count_chars(example).items(), key=lambda x: x[1], reverse=True):
    print('{:3}{:10}'.format(char, count))