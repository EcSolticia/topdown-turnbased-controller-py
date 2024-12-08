
def get_lvl():
	return [
		1, 1, 1, 1, 1, 1, 1, 1,
		1, 0, 0, 0, 0, 1, 0, 1,
		1, 0, 0, 0, 0, 1, 0, 1,
		1, 0, 0, 0, 0, 1, 0, 1,
		1, 0, 0, 1, 0, 1, 0, 1,
		1, 0, 0, 0, 0, 0, 0, 1,
		1, 0, 0, 0, 0, 0, 0, 1,
		1, 1, 1, 1, 1, 1, 1, 1
	]

ind = 9 #position as index

def wall_on_pos(j):
	return (get_lvl()[j] == 1)

def update_display():
	disp = get_lvl()
	disp[ind] = "p"
	
	for i in range(64):
		if disp[i] == 1:
			disp[i] = "#"
		if disp[i] == 0:
			disp[i] = "[]"
	
	for i in range(8):
		print(disp[i*8:i*8 + 8])	

def move_down():
	global ind
	if ind < 48:
		prospective = ind + 8
		if not wall_on_pos(prospective):
			ind = prospective
			
def move_up():
	global ind
	if ind > 16:
		prospective = ind - 8
		if not wall_on_pos(prospective):
			ind = prospective

def move_left():
	global ind
	if ind % 8 > 1:
		prospective = ind - 1
		if not wall_on_pos(prospective):
			ind = prospective
			
def move_right():
	global ind
	if ind % 8 < 7:
		prospective = ind + 1
		if not wall_on_pos(prospective):
			ind = prospective
	
def main():
	update_display()
	
	inp = input("Movement direction?...")
	
	if inp == "a":
		move_left()
	if inp == "d":
		move_right()
	if inp == "w":
		move_up()
	if inp == "s":
		move_down()
	if inp == "n":
		return
	
	main()

main()
