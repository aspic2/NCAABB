# NCAA B[racket]B[uilder] #

BracketBuilder (BB) is a tool built to help you assemble your NCAA Tournament Challenge Bracket this March. It uses information related to each team's performance to determine who will win each round. Support for individualized stats preferences will be added in the future, but for now the primary weight is placed on wins and losses.

### Logic ###
BB ranks teams by using four weighted parameters:

	1. Number of games against Top 25 teams
	2. Number of wins against Top 25 teams
	3. Wins over the last 12 games
	4. Overall season winning percentage

BB will eventually be revised to use any of the stats that ESPN includes with their online bracket. Users will be able to weight the information however they choose, although there will be default settings if no input if given.

### How do I get set up? ###

BB uses Python 3 and Flask. Run the Flask version of the app through app.py.
It is possible to run without Flask by running main.py,
but this will be removed soon.



### License ###
MIT License and all that comes with that.


# NEXT STEPS
This tool is still in development.
The command line version will be phased out soon.

1. Build original functionality into Flask version
  - Build a full bracket and display for the user
2. ~Team vs. Team faceoff options~
3. User input for four weighted parameters.
4. Sanitize user inputs
5. More parameter options?
6. Make it look pretty
