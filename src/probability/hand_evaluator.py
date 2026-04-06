RANK_ORDER = {
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9,
    'T': 10, 'J': 11, 'Q': 12,
    'K': 13, 'A': 14
}

def evaluate_hand(hand):
    values = sorted([RANK_ORDER[c.rank] for c in hand])
    suits = [c.suit for c in hand]

    is_flush = len(set(suits)) == 1

    # Handle sequence (including A-2-3 special case)
    is_sequence = (
        values[0] + 1 == values[1] and values[1] + 1 == values[2]
    ) or values == [2, 3, 14]

    counts = {v: values.count(v) for v in values}

    # Trail (3 same)
    if 3 in counts.values():
        return (5, values)

    # Pure sequence (straight flush)
    if is_sequence and is_flush:
        return (4, values)

    # Sequence
    if is_sequence:
        return (3, values)

    # Color (flush)
    if is_flush:
        return (2, values)

    # Pair
    if 2 in counts.values():
        pair_value = max([v for v in counts if counts[v] == 2])
        return (1, [pair_value] + values)

    # High card
    return (0, values)
