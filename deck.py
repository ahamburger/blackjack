import random

class Deck:
	def __init__(self, card_usage=[], cards_left=[]):
		self.reset()

	def reset(self):
		self._card_usage = [1]*52
		self._cards_left = range(0,52)

	def pickCard(self):
		if len(self._cards_left)==0:
			print "out of cards"	#TODO reshuffle? will this happen?
			return -1

		randomCard = random.randint(0,len(self._cards_left)-1) # random number between 0 and len(cards_left)
		cardIndex = self._cards_left.pop(randomCard)	

		assert _card_usage[cardIndex] == 1, "Card already used"
		
		_card_usage[cardIndex] = 0
		return cardIndex

	def cardify(self, indexNum):
		number = (indexNum % 4) + 1
		if number == 1:
			return "Ace"
		if number <= 10:
			return str(number)
		if number == 11:
			return "Jack"
		if number == 12:
			return "Queen"
		if number == 13:
			return "King"

	def tooFewCards(self):
		return len(self._cards_left) < 10 #TODO this is an arbitrary number at the moment


	#TODO explain ace logic
	def addCards(cardList):
		sum = 0
		haveAce = False
		
		for c in cardList:
			number = (c % 4) + 1
			if number > 10:		# treat jack, queen, king as 10
				number = 10	
			
			if number == 1:
				haveAce = True

			sum += number
				
		if haveAce and (sum + 10 <=21):
			sum += 10		

		return sum
