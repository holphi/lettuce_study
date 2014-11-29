# -*- coding: utf-8 -*-

from lettuce import *
from module import Student
from util import *

@before.each_scenario
def setup_scenario(scenario):
    clearStudentInfo()

@step('Given I have following students in database')
def add_students_to_database(step):
    expected_count = len(step.hashes)
    for stu_dict in step.hashes:
        stu = Student(stu_dict['Id'], stu_dict['Name'],
                          stu_dict['Gender'], stu_dict['Year of birth'],
                          stu_dict['City'])
        insertStudent(stu)
    actual_count = getStudentCount()
    assert actual_count==expected_count, "Got %d" % actual_count

@step('When I query student information by field name "([^"]*)" and value "([^"]*)"')
def query_student_info(step, by, value):
    result = getStudentInfo(by, value)
    world.actual_stu_count = len(result)
    world.actual_result = result

@step('Then I should get (\d+) records in the query result')
def check_query_result_count(step, expected):
    assert world.actual_stu_count == int(expected), 'Got %d records in the result.' % world.actual_stu_count

@step('And I should see the result contains below records')
def check_query_result(step):
    assert world.actual_stu_count == len(step.hashes), 'Got %d records actually.' % world.actual_stu_count
    for stu_dict in step.hashes:
        for stu in world.actual_result:
            if stu.id == stu_dict['Id']:
                assert stu.name == stu_dict['Name'], 'Expected: %s, Actual:%s' % (stu_dict['Name'], stu.name)
                assert stu.gender == stu_dict['Gender'], 'Expected: %s, Actual:%s' % (stu_dict['Gender'], stu.gender)
                assert stu.city == stu_dict['City'], 'Expected: %s Actual: %s' %(stu_dict['City'], stu.city)
                #assert int(stu.year_of_birth) == stu_dict['Year of birth'], 'Expected: %s Actual: %s' %(stu_dict['Year of birth'], stu.year_of_birth)                                                          
                continue
        else:
            return
    assert False, 'Mitmatch result'


