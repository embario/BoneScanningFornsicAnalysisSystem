def should_I_turn_on_the_fans(curr_temp):
	turn_on_fans = False
	# I really hope no MALWARE changes the number in this file...
	with open("fan_temp_const.txt", 'r') as f:
		read_temp = f.readline()
	if curr_temp >= int(read_temp):
		turn_on_fans = True
	return turn_on_fans