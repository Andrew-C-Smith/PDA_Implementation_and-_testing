import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):

        self.ace_spades = Card("spades", 1)
        self.four_spades = Card("spades", 4)
        self.five_spades = Card("spades", 5)

    def test_check_for_ace(self):
        card = self.ace_spades
        self.assertEqual(True, CardGame.check_for_ace(card))

    def test_highest_card(self):
        card1 = self.five_spades
        card2 = self.four_spades
        self.assertEqual(card1, CardGame.highest_card(card1, card2))

    def test_cards_total(self):
        total_cards = [self.ace_spades, self.four_spades, self.five_spades]
        self.assertEqual("You have a total of + 10", CardGame.cards_total(total_cards))