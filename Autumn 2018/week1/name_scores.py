infile = open('names.txt', 'r')
names = []
for line in infile:
    for word in line.split(','):
        names.append(word.strip('"'))

names.sort()

score = 0

for pos, name in enumerate(names):
    alph_val = [ord(char) - 96 for char in name.lower()]
    score += sum(alph_val)*(pos + 1)

print (score)

"""
Terminal> python3 name_scores.py
871198282
"""