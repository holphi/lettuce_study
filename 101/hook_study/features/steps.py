from lettuce import *

@before.all
def say_hello():
    print "Hello there!"
    print "Lettuce will start to run tests right now..."

@after.all
def say_goodbye(total):
    print "Congratulations, %d of %d scenarios passed!" % (
        total.scenarios_ran,
        total.scenarios_passed
    )
    print "Goodbye!"

@before.each_feature
def setup_some_feature(feature):
    print "Running the feature %r, at file %s" % (
        feature.name,
        feature.described_at.file
    )

@after.each_feature
def teardown_some_feature(feature):
    print "The feature %r just has just ran" % feature.name

@before.each_scenario
def setup_some_scenario(scenario):
    print "Running the scenario %r" % scenario.name

@after.each_scenario
def teardown_some_scenario(scenario):
    print "Finishing the scenario %r" % scenario.name

@before.each_step
def setup_some_step(step):
    print "running step %r, defined at %s" % (
        step.sentence,
        step.defined_at.file
    )

@after.each_step
def teardown_some_step(step):
    if not step.hashes:
       print "no tables in the step"

@step('([^"]*)')
def given_i_have_hook_decorator(step, *params):
    pass
