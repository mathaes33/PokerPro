def recommend_action(game_state):
    # Naive rule-based recommendation
    pot = game_state.get('pot', 0)
    actions = game_state.get('actions', [])
    player_count = len(game_state.get('players', []))

    # If few players and pot is small, play aggressive
    if pot < 100 and player_count <= 3:
        return "raise"

    # If pot is big and many players are in, be cautious
    if pot >= 100 and any(act for act in actions if 'raises' in act[1]):
        return "fold"

    # Otherwise, play balanced
    return "call"