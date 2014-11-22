#! /usr/bin/python
from game import Game


if __name__ == "__main__":
	game = Game()
	ready = game.clean_raw_input("Welcome to Blackjack! Ready to play? (y or n) \n")
	if ready == 'y':	
		game.play()