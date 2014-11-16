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
		print("The dealer has been dealt "+ str(self._dCards) + self._deck.stringify(self._dCards))
		print("You've been dealt " + str(self._pCards) + self._deck.stringify(self._pCards))

	def dealOne(self, card_pile):
		card = self._deck.pickCard()
		card_pile.append(card)
		print(self._deck.stringify(card) + "was dealt.")


	#return cards that player has 
	#if busted, removes those cards from deck, start new game
	def playerTurn(self):
		#hit or stay or bust
		move = raw_input("Would you like to hit (h) or stay (s)? \n")
		if move == 'h':
			self.dealOne(self._pCards)
			print self._deck.addCards(self._pCards)
			if self._deck.addCards(self._pCards) > 21:
				print ("Oops, you busted!")	  #TODO: bust? busted?
				self.playAgain(False)
				return	
			print("Now you have "  + str(self._pCards) + self._deck.stringify(self._pCards)) #TODO add acutal cards string			
			self.playerTurn()
		elif move != 's':
			print("Invalid selection. Try again. \n")
			self.playerTurn()


	#return cards that dealer has
	#if busted, removes those cards from deck, start new game
	def dealerTurn(self):
		#hit or stay or bust
		print("The dealer has ... ") #TODO add cards
		sum = self._deck.addCards(self._dCards)
		if sum < 17 or self._deck.isSoftSeventeen(self._dCards):
			self.dealOne(self._dCards)
			if self._deck.addCards(self._dCards) > 21:
				print ("The dealer busted!")	  #TODO: bust? busted?
				self.playAgain(True)
				return	
			print("Okay, now the dealer has ...")	#TODO add acutal cards string			
			self.dealerTurn()
		else:
			print("The dealer's turn is over.")

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
		self.playerTurn()
		self.dealerTurn()

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
		msg = "You lost :( \n"
		if win:		
			self._wins += 1
			msg = "You won! \n"

		msg += "You've won " + self._wins + "times out of " + self._total_rounds + " rounds.\n"
		msg += "That makes your total win percentage: " + str(self._wins/self._total_rounds) + "%. \n"
		again = raw_input(msg + "Would you like to play again? (y or n) \n")
		return again == 'y'
