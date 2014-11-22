from deck import Deck
import sys

### GAME class: controls game play, from dealing to picking a winner. Uses a Deck to keep track of cards.

class Game:
	def __init__(self):
		self._deck = Deck()
		self._pCards = []			#player cards
		self._dCards = []			#dealer cards
		self._round = 1  			#number of rounds (1-6)
		self._wins = 0.0			#total number of wins
		self._total_rounds = 1.0	#total number of rounds (except for ties)


	# Beginning of a new round-- deal 2 cards each to player and dealer
	def deal(self):
		#dealer gets 2 cards
		self._dCards = [self._deck.pickCard(), self._deck.pickCard()]

		#player gets 2 cards
		self._pCards = [self._deck.pickCard(), self._deck.pickCard()]
		
		#Tell player their cards and the "face-up" dealer card
		print("\n*******\nThe dealer has been dealt " + self._deck.stringify(self._dCards, True))
		print("You've been dealt " + self._deck.stringify(self._pCards, False))

	# Add one card from the deck to the parameter pile
	def dealOne(self, card_pile):
		card = self._deck.pickCard()

		if card == -1:	#ran out of cards
			self._deck.shuffleMinus(self._pCards, self._dCards)
			card = self._deck.pickCard()

		card_pile.append(card)

 
	#Returns True if player busted, False otherwise
	#Prompts user to hit or stay. If hit, then asks again. If stay, exits the function. 
	def playerTurn(self):
		move = self.clean_raw_input("\nWould you like to hit (h) or stay (s)? \n(Enter q to quit game.)\n")
		if move == 'h':
			#HIT
			self.dealOne(self._pCards)		#give the player another card

			#BUST
			if self._deck.addCards(self._pCards) > 21:
				print("\n*******\nNow you have "  + self._deck.stringify(self._pCards, False))
				print ("Oops, you busted!\n")
				return True
		
			#prompt again for hit or stay	
			print("\n*******\nNow you have "  + self._deck.stringify(self._pCards, False))	
			return self.playerTurn()
		elif move != 's':
			print("\nInvalid selection. Try again.")
			print("You have "  + self._deck.stringify(self._pCards, False))
			return self.playerTurn()

		#STAY
		return False

	#Returns True if dealer busted, False otherwise
	def dealerTurn(self):
		#sum of current cards
		sum = self._deck.addCards(self._dCards)
		
		if sum < 17 or self._deck.isSoftSeventeen(self._dCards):
			#HIT
			self.dealOne(self._dCards)

			#BUST
			if self._deck.addCards(self._dCards) > 21:
				print("\nThe dealer hits, and now has " + self._deck.stringify(self._dCards, True))
				print("The dealer busted! The dealer's face down card was " + self._deck.cardify(self._dCards[0]) + ".")
				self.clean_raw_input("\nPress ENTER to continue.")
				return True

			print("\nThe dealer hits, and now has " + self._deck.stringify(self._dCards, True))	
			self.clean_raw_input("\nPress ENTER to continue.")
			return self.dealerTurn()

		#STAY
		self.clean_raw_input("\nThe dealer stays. \n\nPress ENTER to continue.");
		return False


	#Determine whether the player wins, the dealer wins, or if there is a tie. Only called when no one busts.
	#Returns string to signify win, loss, tie
	def pickWinner(self):
		#calculate sums of cards
		d_sum = self._deck.addCards(self._dCards)
		p_sum = self._deck.addCards(self._pCards)
		print("\n*******\nYour cards sum to " + str(p_sum) + ", and the dealer's cards sum to " + str(d_sum) + ".")

		if (21-p_sum < 21-d_sum):	#player is closer to 21 than dealer
			return "w"
		elif (21-p_sum == 21-d_sum): #tie
			return "t"
		else:
			return "l"

	
	# Deal cards, then play turns, reveal winner, ask to play again
	def play(self):
		self.deal()

		pBust = self.playerTurn()	#True if player busted (lost, and don't want to have dealer's turn)
		win = "l"

		if not pBust:
			print("\n*******\nThe dealer has "  + self._deck.stringify(self._dCards, True))
			dBust = self.dealerTurn() #True if dealer busted (player won)
			
			if dBust:
				win = "w"
			else:
				win = self.pickWinner() # calculates winner based on sum of card piles

		#ask to play again
		if (self.playAgain(win)):
			#start a new round
			self.newRound()
			self.play()


	#update round numbers, reset player/dealer cards to none
	def newRound(self):
		if (self._round == 6 or self._deck.tooFewCards()):
			self._round = 1
			self._deck = Deck()
		else:
			self._round += 1

		self._total_rounds +=1

		self._pCards = []	
		self._dCards = []	



	#Prompt with win percentage, then ask if want to play again
	#Returns true if opt to play again, false with any other input (ends game)
	def playAgain(self,win):
		status = "LOSE :("
		if win == 'w':
			status = "WIN!"
			self._wins += 1
		elif win == 't':
			self.total_rounds-=1   #don't want to affect our win percentage
			status = "tied with the dealer."


		#Printing of win percentage
		msg = "You " + status + "\n\nYou've won " + str(int(self._wins))	
		#Plurality checking-- "one time" instead of "one times", etc
		if int(self._wins) == 1:
			msg += " time"
		else:
			msg += " times"
		msg += " out of " + str(int(self._total_rounds))

		if  int(self._total_rounds) == 1:
			msg += " round.\n"
		else:
			msg+= " rounds.\n" 

		msg += "That makes your total win percentage: " + str(int(100.0 * self._wins/self._total_rounds)) + "%. \n"

		#ask to play again
		again = self.clean_raw_input(msg + "\nWould you like to play again? (y or n) \n")
		return again == 'y'

	# Helper function so ctrl-D, ctrl-C, or 'q' will quit
	def clean_raw_input(self, string):
		try:
			x = raw_input(string)
			if x == 'q':
				return sys.exit("Quitting")
			return x
		except EOFError:
		    return sys.exit("\nQuitting")
		except KeyboardInterrupt:
			return sys.exit("\nQuitting")

