from lettuce import step
from lettuce import world
from lettuce import *

world.some_variable = 'yay!'

@world.absorb
def add_func(a, b):
    return a + b

@step('When I exemplify "world" by seeing that some variable contain "([^"]*)"')
def exemplify_world(step, value):
    assert world.some_variable == value

@step('When I input number ([^"]*) and ([^"]*)')
def input_value(step, a, b):
    world.result = world.add_func(a, b)

@step('I should receive ([^"]*)')
def check_value(step, expected):
    assert world.result == expected, "Got %s" % world.result

@step('When I invoke spew with parameter "([^"]*)"')
def invoke_spew_with_parameter(step, member_name):
    world.member_name = str(member_name)
    world.spew(member_name)

@step(u'Then I should not see that parameter is bound in the world instance')
def check_is_not_exist(step):
    assert not hasattr(world, world.member_name)