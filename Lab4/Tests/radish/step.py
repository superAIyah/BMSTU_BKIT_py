from radish import given, when, then
from Lab4.fabric import *

@given("I have a truck with speed {speed:g} km/h")
def have_numbers(step, speed):
    step.context.speed = speed

@when("I want it to deliver for {dist:g} km")
def sum_numbers(step, dist):
    step.context.result = dist

@then("I expect the result to be {result:g} h")
def expect_result(step, result):
    assert TruckCreator().factory_method().count_time(step.context.dist) == result