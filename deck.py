class Deck:
	def __init__(self, card_usage=[], cards_left=[]):
		self.reset()

	def reset(self):
		self._card_usage = [1]*52
		self._cards_left = range(0,52)

	def pick_card(self):
		if len(self._cards_left)==0:
			print "out of cards"	#reshuffle? end game?
			return -1

		randomCard = random.randint(0,len(self._cards_left)-1) # random number between 0 and len(cards_left)
		cardIndex = self._cards_left.pop(randomCard)	

		assert _card_usage[cardIndex] == 1, "Card already used"
		
		_card_usage[cardIndex] = 0
		return cardIndex