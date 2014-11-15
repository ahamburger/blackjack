class Game:
	def __init__(self, deck):
		self._deck = deck
		self._pCards = []	#player cards
		self._dCards = []	#dealer cards
		self._round = 0
		self._wins = 0
		self._total_rounds = 0

	def deal(self):
		#dealer gets 2 cards (both face up?)
		self._dCards = [self._deck.pickCard(), self._deck.pickCard()]

		#player gets 2 cards (one face up, one face down)
		self._pCards = [self._deck.pickCard(), self._deck.pickCard()]

		printDCards()
		printPCards()

		move = raw_input("Would you like to hit (h) or stay (s)?")
		if (move == 'h'):


	# player and dealer get cards, pick winner
	def playTurns(self):
		player_cards = playerTurn()	
		dealer_cards = dealerTurn()
		
		return pickWinner()	#True if player won, false if lost


	#return cards that player has 
	#if busted, removes those cards from deck, start new game
	def playerTurn(self):
		#hit or stay or bust
		#raw_input("You've been dealt \n")
		return


	#return cards that dealer has
	#if busted, removes those cards from deck, start new game
	def dealerTurn(self):
		#hit or stay or bust
		return

	def pickWinner(self):
		return

	# round management, deal cards, then play turns
	def play(self):
		if (self._round == 6):
			self._round = 1
			self._deck = reset()
		else:
			self._round += 1

		self._total_rounds +=1

		deal()
		win = playTurns()

		#ask to play again
		if (playAgain(win)):
			play()

	#Prompt with win percentage, then ask if want to play again
	def playAgain(self,win):
		msg = "You lost :( \n"
		if win:		
			self._wins += 1
			msg = "You won! \n"

		msg += "That makes your total win percentage: " + str(self._wins/self._total_rounds) + "%. \n"
		again = raw_input(msg + "Would you like to play again (y or n)? \n")
		return again == 'y'
