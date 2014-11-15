#! /usr/bin/python
import random
from deck import Deck


total_rounds = 0 
wins = 0
#reset deck and remaining cards when starting a new game
def reset():
	return Deck()

def dealOne():
	
	return

def deal(curr_deck):
	#dealer gets 2 cards (both face up?)
	dealer_cards = [curr_deck.pickCard(), curr_deck.pickCard()]

	#player gets 2 cards (one face up, one face down)
	player_cards = [curr_deck.pickCard(), curr_deck.pickCard()]

	print ("The dealer has: " + stringify(dealer_cards))
	print ("You have: " + stringify(player_cards));

	move = raw_input("Would you like to hit (h) or stay (s)?")
	if (move == 'h'):


	return curr_deck

# player and dealer get cards, pick winner
def playTurns(curr_deck, round):
	player_cards = playerTurn(curr_deck)
	curr_deck = updateDeck(curr_deck, player_cards)  #remove cards from deck

	dealer_cards = dealerTurn(curr_deck)
	curr_deck = updateDeck(curr_deck, player_cards)  #remove cards from deck

	return pickWinner(player_cards, dealer_cards)	#True if player won, false if lost


#return cards that player has 
#if busted, removes those cards from deck, start new game
def playerTurn(curr_deck):
	#hit or stay or bust
	#raw_input("You've been dealt \n")
	return


#return cards that dealer has
#if busted, removes those cards from deck, start new game
def dealerTurn(curr_deck):
	#hit or stay or bust
	return

def pickWinner(player, dealer):
	return

# round management, deal cards, then play turns
def play(curr_deck, round):
	if (round == 6):
		round = 1
		curr_deck = reset()
	else:
		round += 1
	global total_rounds
	total_rounds +=1

	curr_deck = deal(curr_deck)
	win = playTurns(curr_deck, round)

	#ask to play again
	if (playAgain(win)):
		play(curr_deck, round)

#Prompt with win percentage, then ask if want to play again
def playAgain(win):
	global wins
	global total_rounds

	msg = "You lost :( \n"
	if win:		
		wins += 1
		msg = "You won! \n"

	msg += "That makes your total win percentage: " + str(wins/total_rounds) + "%. \n"
	again = raw_input(msg + "Would you like to play again (y or n)? \n")
	return again == 'y'

if __name__ == "__main__":
	ready = raw_input("Welcome to Blackjack! Ready to play (y or n)? \n")
	if ready == 'y':
		curr_deck = reset()
		play(curr_deck, 0)



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