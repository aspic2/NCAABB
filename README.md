# NCAA B[racket]B[uilder] #

BracketBuilder (BB) is a tool built to help you assemble your NCAA Tournament Challenge Bracket this March. It uses information related to each team's performance to determine who will win each round. Support for individualized stats preferences will be added in the future, but for now the primary weight is placed on wins and losses.

### Logic ###
BB ranks teams by using four weighted parameters:

	1. Number of games against Top 25 teams
	2. Number of wins against Top 25 teams
	3. Wins over the last 12 games
	4. Overall season winning percentage

BB will eventually be revised to use any of the stats that ESPN includes with their online bracket. Users will be able to weight the information however they choose, although there will be default settings if no input if given.

Scoring logic is now working!

### How do I get set up? ###

BB is written in Python 3. Thanks to a recent Database update, no 3rd party packages are required.


### Licence ###
MIT License and all that comes with that.
