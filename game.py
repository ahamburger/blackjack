from deck import Deck

class Game:
	def __init__(self):
		self._deck = Deck()
		self._pCards = []	#player cards
		self._dCards = []	#dealer cards
		self._round = 1
		self._wins = 0
		self._total_rounds = 1

	def deal(self):
		#dealer gets 2 cards (both face up?)
		self._dCards = [self._deck.pickCard(), self._deck.pickCard()]

		#player gets 2 cards (one face up, one face down)
		self._pCards = [self._deck.pickCard(), self._deck.pickCard()]
		print("\nThe dealer has been dealt " + self._deck.stringify(self._dCards))
		print("You've been dealt " + self._deck.stringify(self._pCards))

	def dealOne(self, card_pile):
		card = self._deck.pickCard()
		card_pile.append(card)
		#print(self._deck.stringify() + "was dealt.")


	#return cards that player has 
	#if busted, removes those cards from deck, start new game
	def playerTurn(self):
		#hit or stay or bust
		move = raw_input("\nWould you like to hit (h) or stay (s)? \n")
		if move == 'h':
			self.dealOne(self._pCards)

			if self._deck.addCards(self._pCards) > 21:
				print("\nNow you have "  + self._deck.stringify(self._pCards))
				print ("Oops, you busted!\n")	  #TODO: bust? busted?
				return 1

			print("\nNow you have "  + self._deck.stringify(self._pCards)) #TODO add acutal cards string			
			self.playerTurn()
		elif move != 's':
			print("Invalid selection. Try again. \n")
			self.playerTurn()

		return 0

	#return cards that dealer has
	#if busted, removes those cards from deck, start new game
	def dealerTurn(self):
		#hit or stay or bust
		print("\nThe dealer has "  + self._deck.stringify(self._dCards))
		sum = self._deck.addCards(self._dCards)
		if sum < 17 or self._deck.isSoftSeventeen(self._dCards):
			self.dealOne(self._dCards)
			if self._deck.addCards(self._dCards) > 21:
				print("\nNow the dealer has " + self._deck.stringify(self._dCards))
				print ("The dealer busted!")	  #TODO: bust? busted?
				return 1
			print("\nNow the dealer has " + self._deck.stringify(self._dCards))	
			self.dealerTurn()
		else:
			print("The dealer's turn is over.")
		return 0

	def pickWinner(self):
		d_sum = self._deck.addCards(self._dCards)
		p_sum = self._deck.addCards(self._pCards)
		
		if (21-p_sum < 21-d_sum):	#player is closer to 21 than dealer
			return True
		elif (21-p_sum == 21-d_sum): #tie--- TODO find out what todo
			return False
		else:
			return False

	
	# deal cards, then play turns
	def play(self):
		self.deal()

		pBust = self.playerTurn()

		win = False
		if pBust == 0:
			dBust = self.dealerTurn()

			if dBust == 1:
				win = True
			else:
				win = self.pickWinner() #True if player won, false if lost

		#ask to play again
		if (self.playAgain(win)):
			self.reset()
			self.play()


	#update round numbers, reset player/dealer cards to none
	def reset(self):
		if (self._round == 6 or self._deck.tooFewCards()):
			self._round = 1
			self._deck = Deck()
		else:
			self._round += 1

		self._total_rounds +=1

		self._pCards = []	
		self._dCards = []	



	#Prompt with win percentage, then ask if want to play again
	def playAgain(self,win):
		msg = "\nYou LOST :( \n"
		if win:		
			self._wins += 1
			msg = "\nYou WON! \n"

		msg += "\n You've won " + str(self._wins) + " times out of " + str(self._total_rounds) + " rounds.\n" #TODO adjust plurality
		msg += "That makes your total win percentage: " + str(self._wins/self._total_rounds) + "%. \n"
		again = raw_input(msg + "\nWould you like to play again? (y or n) \n")
		return again == 'y'
