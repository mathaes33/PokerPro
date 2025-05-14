from treys import Evaluator, Card, Deck

def evaluate_equity(hero_hand, num_simulations=1000):
    evaluator = Evaluator()
    deck = Deck()

    # Remove hero cards
    for card in hero_hand:
        deck.cards.remove(Card.new(card))

    hero_score = 0

    for _ in range(num_simulations):
        deck.shuffle()
        villian_hand = [deck.draw(1)[0], deck.draw(1)[0]]
        board = deck.draw(5)
        score_hero = evaluator.evaluate(board, [Card.new(card) for card in hero_hand])
        score_villain = evaluator.evaluate(board, villian_hand)

        if score_hero < score_villain:
            hero_score += 1
        elif score_hero == score_villain:
            hero_score += 0.5

    return hero_score / num_simulations