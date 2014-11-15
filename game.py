from deck import Deck

class Game:
	def __init__(self, deck):
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
		# print("The dealer has been dealt " + _self._deck.stringify(self._dCards))
		# print("You've been dealt" +  _self._deck.stringify(self._pCards))

	#return cards that player has 
	#if busted, removes those cards from deck, start new game
	def playerTurn(self):
		#hit or stay or bust
		move = raw_input("Would you like to hit (h) or stay (s)? \n")
		if move == 'h':
			dealOne()
			if p_sum > 21:
				print ("Oops, you busted!")	  #TODO: bust? busted?
				playAgain(False)
				return	
			print("Okay, now you have ...")	#TODO add acutal cards string			
			playerTurn()
		elif move != 's':
			print("Invalid selection. Try again. \n")
			playerTurn()


	#return cards that dealer has
	#if busted, removes those cards from deck, start new game
	def dealerTurn(self):
		#hit or stay or bust
		return

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
		deal()
		playerTurn()
		dealerTurn()

		win = pickWinner() #True if player won, false if lost

		#ask to play again
		if (playAgain(win)):
			reset()
			play()


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

		msg += "That makes your total win percentage: " + str(self._wins/self._total_rounds) + "%. \n"
		again = raw_input(msg + "Would you like to play again? (y or n) \n")
		return again == 'y'
