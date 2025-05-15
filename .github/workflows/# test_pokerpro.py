import unittest
from pokerpro import Card, Deck,class TestCard(unittest.TestCase):

    def test_card_creation(self):
        card = Card("A", "h")
        self.assertEqual(card.rank, "A")
        self.assertEqual(card.suit, "h")

    def test_card_representation(self):
        card = Card("K", "d")
        self.assertEqual(str(card), "Kd")

    def test_card_comparison(self):
        card1 = Card("T", "s")
        card2 = Card("T", "c")
        card3 = Card("J", "s")
        self.assertEqual(card1, card2)
        self.assertNotEqual(card1, card3)
        self.assertTrue(card1 <= card2)
        self.assertTrue(card1 >= card2)
        self.assertTrue(card1 < card3)
        self.assertTrue(card3 > card1)

class TestDeck(unittest.TestCase):

    def test_deck_creation(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_deal_card(self):
        deck = Deck()
        card = deck.deal_card()
        self.assertIsInstance(card, Card)
        self.assertEqual(len(deck.cards), 51)

    def test_deck_shuffle(self):
        deck1 = Deck()
        deck2 = Deck()
        deck2.shuffle()
        self.assertNotEqual(deck1.cards, deck2.cards)

class TestHand(unittest.TestCase):

    def test_hand_creation(self):
        cards = [Card("A", "s"), Card("K", "h"), Card("Q", "d"), Card("J", "c"), Card("T", "s")]
        hand = Hand(cards)
        self.assertEqual(len(hand.cards), 5)

    def test_hand_add_card(self):
        hand = Hand([])
        card1 = Card("2", "s")
        card2 = Card("3", "h")
        hand.add_card(card1)
        hand.add_card(card2)
        self.assertEqual(len(hand.cards), 2)
        self.assertIn(card1, hand.cards)
        self.assertIn(card2, hand.cards)

    # Add more tests for hand evaluation logic here
    # For example:
    # def test_is_straight_flush(self):
    #     cards = [Card("A", "h"), Card("K", "h"), Card("Q", "h"), Card("J", "h"), Card("T", "h")]
    #     hand = Hand(cards)
    #     self.assertTrue(hand.is_straight_flush())

    # def test_is_four_of_a_kind(self):
    #     cards = [Card("A", "s"), Card("A", "h"), Card("A", "d"), Card("A", "c"), Card("2", "s")]
    #     hand = Hand(cards)
    #     self.assertTrue(hand.is_four_of_a_kind())

    # ... and so on for other hand rankings


if __name__ == '__main__':
    unittest.main()