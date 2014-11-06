from lettuce import step
from lettuce import world
from lettuce import *

world.some_variable = 'yay!'

@world.absorb
def add(a, b):
    return a + b

@step('When I exemplify "world" by seeing that some variable contain "([^"]*)"')
def exemplify_world(step, value):
    assert world.some_variable == value

@step('When I input number (\d+) and (\d+)')
def input_value(step, a, b):
    world.result = world.add(a, b)

@step('I should get (\d+)')
def check_value(step, expected):
    assert world.result == expected, "Got %s" % world.result

@step('When I invoke spew() with parameter "([^"]*)"')
def invoke_spew_with_parameter(step, member_name):
    world.member_name = str(member_name)
    world.spew(member_name)
    
@step('Then it should not see it''s bound in the world object')
def check_membmer_removed_from_the_world(step):
    assert False, 'This step must be implemented'

@step(u'When I invoke world.spew() with parameter "([^"]*)"')
def when_i_invoke_world_spew_with_parameter_group1(step, group1):
    world.member_name = str(member_name)
    world.spew(member_name)
    
@step(u'Then it should not see it''s bound in the world object')
def then_it_should_not_see_it_s_bound_in_the_world_object(step):
    assert False, 'This step must be implemented'