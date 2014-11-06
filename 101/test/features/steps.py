from lettuce import *

@step('I have the number (\d+)')
def have_the_number(step, number):
    world.number = int(number)

@step('I compute its factorial')
def compute_its_factorial(step):
    world.number = factorial(world.number)

@step('I see the number (\d+)')
def check_number(step, expected):
    expected = int(expected)
    assert world.number == expected, "Got %d" % world.number

@step('Given I have the string ([^"]*)')
def have_the_string(step, s):
    world.str_val = str(s)

@step('When I put it in upper case')
def change_to_upper_case(step):
    world.str_val = world.str_val.upper()
    
@step('Then I should see the string is ([^"]*)')
def check_uppercase(step, expected):
    assert world.str_val == expected, "Got %s" % world.str_val
    
def factorial(number):
    number = int(number)
    if(number==0) or (number==1):
        return 1
    else:
        return number*factorial(number-1)
