Feature: test lettuce's world

	Scenario: check world's variable
		When I exemplify "world" by seeing that some variable contain "yay!"

	Scenario: check world.spew
		When I invoke spew with parameter "add"
		Then I should not see that parameter is bound in the world instance
	
	Scenario Outline: check world.absorb
		When I input number <a> and <b>
		Then I should receive <expected>
		
	Examples:
		|a			|b			|expected		|
		|abc		|defg		|abcdefg		|
		|Hello, 	|world		|Hello,world	|
		|5			|3			|8				|
		|@@			|~~			|@@~~			|
		