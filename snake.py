import random
import curses

class snakeGame:

	def __init__(self, height, width):
		self.shell_h = height 
		self.shell_w = width

		if(height < 30 or width < 60):
			raise ValueError("Minimum shell size requirements not met")
		self.snk_x = int(width / 3)
		self.snk_y = int(height / 2) 
		self.score = 0
		self.snake = [[self.snk_y, self.snk_x], [self.snk_y, self.snk_x-1], [self.snk_y, self.snk_x-2]]
		self.food = [int(width / 2), int(height/2)]

	def initWindow(self):
		curses.initscr()
		curses.curs_set(0)
		window = curses.newwin(self.shell_h, self.shell_w, 0, 0)
		window.keypad(1) 	#Accpet keypad inputs
		window.timeout(100) #Set refresh rate

		#Reset game variables
		self.snk_x = int(self.shell_w / 3)
		self.snk_y = int(self.shell_h / 2) 
		self.score = 0
		self.snake = [[self.snk_y, self.snk_x], [self.snk_y, self.snk_x-1], [self.snk_y, self.snk_x-2]]
		self.food = [int(self.shell_h / 2), int(self.shell_w/2)]


		window.addch(int(self.food[0]), int(self.food[1]), curses.ACS_PI)

		return window

	def playGame(self):
		window = self.initWindow()
		key = curses.KEY_RIGHT

		while True:
			next_key = window.getch()
			key = key if next_key == -1 else next_key

			# Check if snake is out of bounds or has consumed itself
			if (self.snake[0][0] in [0, self.shell_h] 
				or self.snake[0][1] in [0, self.shell_w] 
				or self.snake[0] in self.snake[1:]):
				window.addstr(int(self.shell_h/8), int(self.shell_w/2), "Game Over Score:{0}".format(self.score))
				window.addstr(int(self.shell_h/8 + 1), int(self.shell_w/2), "Would you like to play again?")
				window.addstr(int(self.shell_h/8 + 2), int(self.shell_w/2), "y/n")
				while True:
					next_key = window.getch()
					key = key if next_key == -1 else next_key
					if key == ord('y'):
						window.clear()
						window = self.initWindow()
						key = curses.KEY_RIGHT
						break
					if key == ord('n'):
						curses.endwin()
						quit()

			new_head = [self.snake[0][0], self.snake[0][1]]

			# Keys pertaining to movement
			if key == curses.KEY_DOWN:
				new_head[0] += 1
			if key == curses.KEY_UP:
				new_head[0] -= 1
			if key == curses.KEY_LEFT:
				new_head[1] -= 1
			if key == curses.KEY_RIGHT:
				new_head[1] += 1
			# 'q' to quit
			if key == ord('q'):
				curses.endwin
				quit()

			self.snake.insert(0, new_head)

			if self.snake[0] == self.food:
				self.score += 1
				self.food = None
				while self.food is None:
					newFood = [
						random.randint(1, self.shell_h - 1),
						random.randint(1, self.shell_w - 1)
					]
					self.food = newFood if newFood not in self.snake else None
					#Add food character to the window
					window.addch(int(self.food[0]), int(self.food[1]), curses.ACS_PI)
			else:
				tail = self.snake.pop()
				window.addch(int(tail[0]), int(tail[1]), ' ')

			window.addch(int(self.snake[0][0]), int(self.snake[0][1]), curses.ACS_CKBOARD)

def main(stdscr):
	max_y, max_x = stdscr.getmaxyx()
	print (max_y)
	print (max_x)
	game = snakeGame(max_y, max_x)
	game.playGame()

curses.wrapper(main)
