from sys import argv
from collections import defaultdict
input = argv[1] if len(argv) > 1 else 'input.txt'

with open(input) as f:
    lines = [line.strip() for line in f.readlines()]

totpoints = 0
cards, card_amount = set(), defaultdict(int)
for line in lines:
    card_id = int(line.split(':')[0].split()[1])
    cards.add(card_id)
    card_amount[card_id] += 1
    card_numbers = line.split(':')[1].split('|')[0].split()
    my_numbers = line.split('|')[1].split()
    matches = len(set(card_numbers) & set(my_numbers))
    totpoints += int(2**(matches-1))
    for copy in range(card_id+1, card_id + matches+1):
        card_amount[copy] += card_amount[card_id]

totcards = sum({k: card_amount[k] for k in cards}.values())
print(f'Total points: {totpoints}')
print(f'Total cards: {totcards}')
