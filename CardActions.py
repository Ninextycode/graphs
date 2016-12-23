cards = [i for i in range(52)]


def possible_next_cards(current_cards):
    if len(current_cards) > 0:
        highest_card = max(current_cards)
        possible_cards = cards[highest_card + 1:]
    else:
        possible_cards = cards[:]

    return possible_cards


def add_card(current_cards, card):
    current_cards.append(card)
    return current_cards
