#! /usr/bin/python
import random
from deck import Deck


#reset deck and remaining cards when starting a new game
def reset():
	return Deck()

def dealOne():
	
	return

def deal(curr_deck):
	#dealer gets 2 cards (both face up?)
	#player gets 2 cards (one face up, one face down)
	return curr_deck

def playGame():
	player_sum = playerTurn()
	dealer_sum = dealerTurn()
	pickWinner(player_sum, dealer_sum)
	reset()
	return

def playerTurn():
	#hit or stay or bust
	return

def dealerTurn():
	#hit or stay or bust
	return

def pickWinner(player, dealer):
	return

def play(round):
	# if (round == 6):
	# 	round = 1
	# 	curr_deck = reset()
	# else:
	# 	round += 1
		
	curr_deck = deal(curr_deck)
	playGame(curr_deck)

if __name__ == "__main__":
	play(0)



#Notes:
# TODO
	# -- keep track of round number (new deck after 6)
	# -- keep track of win percentage

# list of size 52, containing all 1s to start
# As card is used, set index to 0

# Hearts: 1st 13 indices (0-12)
# Diamonds: 2nd 13 indices (13-25)
# Clubs: 3rd 13 indices (26-38)
# Spades: 4th 13 indices (39-51)

# ie for hearts
# 0: ace, 1: 2, 2: 3 ... 9: 10, 10: jack, 11: queen, 12: king

# also make a list of the numbers 1-52
# to pick a new card, select random int b/w 0 and size of list
# remove the number at that index from  list of numbers
# use that number to index into the list of 1s 