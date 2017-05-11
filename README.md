# NCAA B[racket]B[uilder] #

BracketBuilder (BB) is a tool built to help you assemble your NCAA Tournament Challenge Bracket this March. It uses information related to each team's performance to determine who will win each round. Support for individualized stats preferences will be added in the future, but for now the primary weight is placed on wins and losses.

### Logic ###
BB currently uses my two favorite metrics to determine which team is most likely to win:

	1. Past 12 games record (weighted .5)
	2. vs. top 25 teams record (weighted .5)

BB will eventually be revised to use any of the stats that ESPN includes with their online bracket. Users will be able to weight the information however they choose, although there will be default settings if no input if given.

### How do I get set up? ###

BB is written in Python 3 and requires the following packages to run:  
- pypyodbc (for database calls)


### Licence ###
Coming soon
