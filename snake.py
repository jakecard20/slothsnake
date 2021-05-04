import random
import curses

shell = curses.initscr()
curses.curs_set(0)
shell_height, shell_width = shell.getmaxyx()

window = curses.newwin(shell_height, shell_width, 0, 0)

window.keypad(1) 	#Accpet keypad inputs

window.timeout(100) #Set refresh rate


snk_x = shell_width/4
snk_y = shell_height/2
snake = [
	[snk_y, snk_x],
	[snk_y, snk_x - 1],
	[snk_y, snk_x - 2]
	]
print(snake)
food = [shell_height/2, shell_width/2]
print(int(food[0]))
print(int(food[1]))
print(curses.ACS_PI)
window.addch(int(food[0]), int(food[1]), '@')
#window.addch(curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
	next_key = window.getch()
	key = key if next_key == -1 else next_key

	if snake[0][0] in [0, shell_height] or snake[0][1] in [0, shell_width] or snake[0] in snake[1:]:
		curses.endwin()
		quit()

	new_head = [snake[0][0], snake[0][1]]

	if key == curses.KEY_DOWN:
		new_head[0] += 1
	if key == curses.KEY_UP:
		new_head[0] -= 1
	if key == curses.KEY_LEFT:
		new_head[1] -= 1
	if key == curses.KEY_RIGHT:
		new_head[1] += 1

	snake.insert(0, new_head)

	if snake[0] == food:
		food = None
		while food is None:
			newFood = [
				random.randint(1, shell_height - 1),
				random.randint(1, shell_width - 1)
			]
			food = newFood if newFood not in snake else None
			window.addch(int(food[0]), int(food[1]), curses.ACS_PI)
	else:
		tail = snake.pop()
		window.addch(int(tail[0]), int(tail[1]), ' ')

	window.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)