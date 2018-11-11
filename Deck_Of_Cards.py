from random import shuffle
class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __repr__(self):
		return f"{self.value} of {self.suit}"

class deck:
	suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
	values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
	def __init__(self):
		cards = []
		for deck.suit in deck.suits:
			for deck.value in deck.values:
				cards.append(Card(deck.suit, deck.value))
		self.cards = cards

	def __repr__(self):
		return f"deck of {len(self.cards)} cards"

	def count(self):
		return len(self.cards)

	def _deal(self, num = 1):
		if len(self.cards) <= 0:
			raise ValueError("All cards have been dealt")
		elif num > 1:
			return [self.cards.pop() for i in range(num) if len(self.cards) > 0]
		return self.cards.pop()

	def shuffle(self):
		if len(self.cards) != 52:
			raise ValueError("Only Full decks can be shuffled")
		else:
			shuffle(self.cards)
			return self

	def deal_card(self):
		return self._deal()

	def deal_hand(self, num):
		return self._deal(num)