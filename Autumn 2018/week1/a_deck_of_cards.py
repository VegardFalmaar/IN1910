import random

suits = ['H', 'D', 'C', 'S']
deck = []

for num in range(1, 14):
    deck += [(num, suit) for suit in suits]

random.shuffle(deck)

drawn = deck[:13]

# print (deck)

for suit_ in suits:
    sort = []
    for card in drawn:
        val, suit = card
        if suit == suit_:
            sort.append(card)
    for card in sorted(sort):
        print (card)
