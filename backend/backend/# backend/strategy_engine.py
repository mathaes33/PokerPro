# backend/strategy_engine.py

import random
from poker import Card, Deck, Hand

def calculate_hand_equity(player_hand, community_cards, num_simulations=10000):
    wins = 0
    for _ in range(num_simulations):
        deck = Deck()
        deck.remove_cards(player_hand + community_cards)
        opponent_hand = deck.draw(2)
        remaining_community = deck.draw(5 - len(community_cards))
        full_community = community_cards + remaining_community

        player_best = Hand(player_hand + full_community).best_hand()
        opponent_best = Hand(opponent_hand + full_community).best_hand()

        if player_best > opponent_best:
            wins += 1
    return wins / num_simulations

def recommend_action(hand_equity, pot_odds):
    if hand_equity > pot_odds:
        return 'call'
    else:
        return 'fold'