Feature: test lettuce's world

	Scenario: check world's variable
		When I exemplify "world" by seeing that some variable contain "yay!"

	Scenario: check world.spew
		When I invoke spew() with parameter "add"
		Then it should not see it's bound in the world object