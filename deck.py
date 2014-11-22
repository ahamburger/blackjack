import random

#DECK class: keeps track of cards available and picking cards to deal

# Note: 
# self._cards_left is a list of numbers 0-51

# each set of 13 indices represents a different suit of cards.
# For example-- 
# Hearts: 1st 13 indices (0-12) -- 0: ace, 1: 2, 2: 3 ... 9: 10, 10: jack, 11: queen, 12: king
# Diamonds: 2nd 13 indices (13-25)
# Clubs: 3rd 13 indices (26-38)
# Spades: 4th 13 indices (39-51)

# to pick a new card, select random int between 0 and size of self._cards_left 
# use whatever number is at that index (and remove that number) as drawn card

class Deck:
	def __init__(self, cards_left=[]):
		self.reset()

	#make all cards available
	def reset(self):
		self._cards_left = range(0,52)		# each value 0-51 correlates with a unique card. cards are removed from this list as they 
											# are used.

	#reset all cards except those in the parameter card lists
	#do this by restoring all cards to cards_left, then removing those in the two specified card lists
	def shuffleMinus(self, cardList1, cardList2):
		self.reset()
		for c in cardList1:
			self._cards_left.remove(c)
		for c2 in cardList2:
			self._cards_left.remove(c2)

	# returns index (0-51) of randomly selected card from remaining deck
	# if there are no cards left, return -1
	def pickCard(self):
		if len(self._cards_left)==0:
			return -1

		randomCard = random.randint(0,len(self._cards_left)-1) # random number between 0 and len(cards_left)
		cardIndex = self._cards_left.pop(randomCard)	

		return cardIndex

	#returns string representing the value of the card ie "a 2" or "an 8" or "a Jack"
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

	#returns true if there are fewer than 5 cards left in the deck 
	def tooFewCards(self):
		return len(self._cards_left) < 5


	#returns the sum of the cards (represented as their card indices, 0-51) in cardList
	#evaluates Aces so that use as 11 if that sum is closer to 21 (but not over)
	def addCards(self, cardList):
		sum = 0
		haveAce = False		#used to keep track of if there is an ace in the hand
		
		for c in cardList:
			number = (c % 13) + 1 	#convert to numerical value of card instead of card index
			if number > 10:		# treat jack, queen, king as 10
				number = 10	
			
			if number == 1:
				haveAce = True

			sum += number
				
		# if there's one or more aces, check to see if counting one ace as an 11 will be beneficial
		if haveAce and (sum + 10 <=21):
			sum += 10		

		return sum


	#returns true if the cardList contains exactly one 6 and one Ace
	def isSoftSeventeen(self,cardList):
		if not len(cardList) == 2:		#short circuit if more than 2 cards
			return False

		#convert to numerical value of card instead of card index
		card1 = (cardList[0]%13) + 1
		card2 = (cardList[1]%13) + 1
		
		if (card1 == 6 and card2 == 1) or (card1 == 1 and card2 == 6):
			return True
		return False

	#Return a string that is a sentence describing the cards in cardList. If faceDown is true, then conceal the first
	#card in the list
	def stringify(self, cardList, faceDown):
		cards = ""
		comma = ", "
		if len(cardList) == 2:		#so will say "a 2 and a 7" instead of "a 2, and a 7" if there are only two cards
			comma = " "

		for c in cardList:
			if c == cardList[0] and faceDown:
				continue			
			elif c == cardList[-1] and not faceDown:	#last card. If face down then we don't want the "and" 
				cards += "and " + self.cardify(c) + "."
			else:
				cards += self.cardify(c)+ comma

		if faceDown:
			cards += "and a face down card."
		return cards
