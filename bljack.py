#! /usr/bin/python
from game import Game


if __name__ == "__main__":
	ready = raw_input("Welcome to Blackjack! Ready to play? (y or n) \n")
	if ready == 'y':
		game = Game()
		game.play()



#Notes:
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