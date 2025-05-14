def classify_hand(card1, card2):
    """
    Takes two hole cards and classifies them into poker hand groups.
    Assumes input like 'Ah', 'Ks', etc.
    """
    rank1, suit1 = card1[0], card1[1]
    rank2, suit2 = card2[0], card2[1]
    suited = suit1 == suit2

    ranks = sorted([rank1, rank2], reverse=True)
    hand = ''.join(ranks)
    if suited:
        hand += 's'
    else:
        hand += 'o'

    return hand

# Simplified preflop hand categories
strong_hands = {'AA', 'KK', 'QQ', 'JJ', 'AKs'}
medium_hands = {'TT', '99', '88', 'AQs', 'AJs', 'KQs', 'AKo'}
speculative_hands = {'77', '66', '55', 'AJo', 'KQo', 'ATs', 'KJs'}

def recommend_action(game_state):
    # Expecting hero's hand in game_state
    hero = game_state.get('hero', {'hand': ['Ah', 'Kd']})
    card1, card2 = hero['hand']
    hand_type = classify_hand(card1, card2)

    pot = game_state.get('pot', 0)
    player_count = len(game_state.get('players', []))

    if hand_type in strong_hands:
        return "raise"
    elif hand_type in medium_hands:
        return "call" if pot <= 200 else "fold"
    elif hand_type in speculative_hands:
        return "call" if player_count >= 4 and pot < 100 else "fold"
    else:
        return "fold"