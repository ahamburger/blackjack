#! /usr/bin/python
import random
deck=[]
cards_left=[]


#reset deck and remaining cards when starting a new game
def reset():
	global deck
	global cards_left

	deck = [1]*52
	cards_left = range(0,52)



def deal():
	global deck
	global cards_left

	i = 0
	while i <= 52:
		i+=1
		pick_card()

def pick_card():
	global deck
	global cards_left

	if len(cards_left)==0:
		print "out of cards"	#reshuffle? end game?
		return

	randomCard = random.randint(0,len(cards_left)-1) # random number between 0 and len(cards_left)
	cardIndex = cards_left.pop(randomCard)	
	
	assert deck[cardIndex] == 1, "Card already used"
	
	deck[cardIndex] = 0
	return cardIndex

if __name__ == "__main__":
	reset()
	deal()



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