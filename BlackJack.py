import random

cards = lambda: random.randint(1, 13) #lambda function to call random

def card_value(card):
    if card > 10:
        return 10
    elif card == 1:
        return 11
    else:
        return card
    
def hand(hand):
    total = 0
    ace = 0
    for i in hand:
        value = card_value(i)
        total += value
        if i == 1 or i == 11:
            ace += 1

    while total > 21 and ace > 0:
        total -= 10
        ace -= 1
    return total

dealer = [cards(), cards()]

player = [cards(), cards()]

print(f"Dealer shows: {dealer[0]}")
print(f"Your cards: {player} (value {hand(player)})")


while True:
    hit = input("Do you want to hit?(yes/no) ")
    if hit.lower() == "yes":
        if hand(player) > 21:
            print("You lose")
            break
        player.append(cards())
        print(f"After hit: {player} (value {hand(player)})")
    else:
        print(f"Dealers current hand {dealer} (value {hand(dealer)})")
        break

while hand(dealer) < 17 and hand(player) < 21 and hand(dealer) < hand(player):
    dealer.append(cards())
    print(f"Dealers current hand {dealer} (value {hand(dealer)})")
    if hand(dealer) > 21:
        print("Dealers hand is over 21 you win")    
        break


if hand(player) > hand(dealer):
    print("You win!")
elif hand(player) < hand(dealer):
    print("You lose!")
else:
    print("Tie!")