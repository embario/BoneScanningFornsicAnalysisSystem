from should_I_turn_on_the_fans import *
import pytest
import ipdb

def test_turn_fans_on_with_exact_temp():
	assert should_I_turn_on_the_fans(75) == True

def test_do_not_turn_fans_on():
	assert should_I_turn_on_the_fans(50) == False

def test_NOOOOO():
	assert should_I_turn_on_the_fans(75) == True

	with open("fan_temp_const.txt", "w") as f:
		f.write("750")

	assert should_I_turn_on_the_fans(740) == False

	with open("fan_temp_const.txt", "w") as f:
		f.write("75")	