from deck import Deck

class Game:
	def __init__(self):
		self._deck = Deck()
		self._pCards = []	#player cards
		self._dCards = []	#dealer cards
		self._round = 1
		self._wins = 0.0
		self._total_rounds = 1.0

	def deal(self):
		#dealer gets 2 cards (both face up?)	TODO make one face down?
		self._dCards = [self._deck.pickCard(), self._deck.pickCard()]

		#player gets 2 cards (one face up, one face down)
		self._pCards = [self._deck.pickCard(), self._deck.pickCard()]
		print("\n*******\nThe dealer has been dealt " + self._deck.stringify(self._dCards))
		print("You've been dealt " + self._deck.stringify(self._pCards))

	def dealOne(self, card_pile):
		card = self._deck.pickCard()
		card_pile.append(card)


	#return cards that player has 
	#if busted, removes those cards from deck, start new game
	def playerTurn(self):
		#hit or stay or bust
		move = self.clean_raw_input("\nWould you like to hit (h) or stay (s)? \n")
		if move == 'h':
			self.dealOne(self._pCards)

			if self._deck.addCards(self._pCards) > 21:
				print("\n*******\nNow you have "  + self._deck.stringify(self._pCards))
				print ("Oops, you busted!\n")
				return True

			print("\n*******\nNow you have "  + self._deck.stringify(self._pCards))		
			return self.playerTurn()
		elif move != 's':
			print("Invalid selection. Try again. \n")
			return self.playerTurn()

		return False

	#return cards that dealer has
	#if busted, removes those cards from deck, start new game
	def dealerTurn(self):
		#hit or stay or bust
		sum = self._deck.addCards(self._dCards)
		
		if sum < 17 or self._deck.isSoftSeventeen(self._dCards):
			self.dealOne(self._dCards)
			if self._deck.addCards(self._dCards) > 21:
				print("\nThe dealer hits, and now has " + self._deck.stringify(self._dCards))
				print("The dealer busted!")
				self.clean_raw_input("\nPress ENTER to continue.")
				return True
			print("\nThe dealer hits, and now has " + self._deck.stringify(self._dCards))	
			self.clean_raw_input("\nPress ENTER to continue.")
			return self.dealerTurn()
		else:
			self.clean_raw_input("\nThe dealer stays. \n\nPress ENTER to continue.");

		
		return False

	def pickWinner(self):
		d_sum = self._deck.addCards(self._dCards)
		p_sum = self._deck.addCards(self._pCards)
		
		if (21-p_sum < 21-d_sum):	#player is closer to 21 than dealer
			self._wins += 1.0
			return "WIN!"
		elif (21-p_sum == 21-d_sum): #tie
			self.total_rounds-=1   #don't want to affect our win percentage
			return "and the dealer TIE."
		else:
			return "LOSE :("

	
	# deal cards, then play turns
	def play(self):
		self.deal()

		pBust = self.playerTurn()

		win = "LOSE :("
		if not pBust:
			print("\n*******\nThe dealer has "  + self._deck.stringify(self._dCards))
			dBust = self.dealerTurn()

			if dBust:
				win = "WIN!"
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
		msg = "*******\nYou " + win + "\n"


		msg += "\nYou've won " + str(int(self._wins)) + " times out of " + str(int(self._total_rounds)) + " rounds.\n" #TODO adjust plurality
		msg += "That makes your total win percentage: " + str(int(100.0 * self._wins/self._total_rounds)) + "%. \n"
		again = self.clean_raw_input(msg + "\nWould you like to play again? (y or n) \n")
		return again == 'y'

	def clean_raw_input(self, string):
		try:
			return raw_input(string)
		except EOFError:
			return "\nQuitting"
		except KeyboardInterrupt:
			return "\nQuitting"

