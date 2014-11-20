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

		assert self._card_usage[cardIndex] == 1, "Card already used"
		
		self._card_usage[cardIndex] = 0
		return cardIndex

	def cardify(self, indexNum):
		number = (indexNum % 13) + 1
		if number == 1:
			return "an Ace"
		if number == 8:
			return "an 8"

		if number <= 10:
			return "a " + str(number)
		if number == 11:
			return "a Jack"
		if number == 12:
			return "a Queen"
		if number == 13:
			return "a King"

	def tooFewCards(self):
		return len(self._cards_left) < 5


	#TODO explain ace logic
	def addCards(self, cardList):
		sum = 0
		haveAce = False
		
		for c in cardList:
			number = (c % 13) + 1
			if number > 10:		# treat jack, queen, king as 10
				number = 10	
			
			if number == 1:
				haveAce = True

			sum += number
				
		if haveAce and (sum + 10 <=21):
			sum += 10		

		return sum

	def isSoftSeventeen(self,cardList):
		if not len(cardList) == 2:
			return False
		card1 = (cardList[0]%13) + 1
		card2 = (cardList[1]%13) + 1
		
		if (card1 == 6 and card2 == 1) or (card1 == 1 and card2 == 6):
			return True
		return False

	def stringify(self, cardList):	#an 8 an ace
		cards = ""
		for c in cardList:			
			if c == cardList[-1]:	#last card
				cards += "and " + self.cardify(c) + "."
			else:
				cards += self.cardify(c)+ ", "
		return cards
