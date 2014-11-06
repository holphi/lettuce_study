Feature: Upper case operation for string
 
	In order to play with Lettuce
	As beginners
	We'll implement upper case operation for string

	Scenario Outline: Upper case operation
		Given I have the string <input>
		When I put it in upper case
		Then I should see the string is <expected>
	
	Examples:
		|input			|expected		|
		|lettuce leaves	|LETTUCE LEAVES	|
		|Hello woRLd		|HELLO WORLD		|
		|#$$#%#$%#$%#$	|#$$#%#$%#$%#$	|
		|1234567890		|1234567890		|
		|LETTUCE			|LETTUCE			|
		|abc				|ABc				|