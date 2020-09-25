from pygame.draw import rect
import random

class Cell:
	def __init__(self, i, j):
		self.i = i
		self.j = j
		self.wall = random.uniform(0, 1) < 0.45
		# infinity default values
		self.g_score = 9999999999999999999999999
		self.f_score = 9999999999999999999999999
		self.parent = None
		self.visited = False
		return

	def draw(self, width, height, scr):
		if not self.wall and not self.visited:
			rect(scr, (255, 255, 255), (self.i * width + 25, self.j * height + 25, width - 2, height - 2), 2)
		elif self.visited:
			rect(scr, (255, 0, 0), (self.i * width + 25, self.j * height + 25, width - 2, height - 2))
		return

	def draw_green(self, width, height, scr):
		rect(scr, (0, 255, 0), (self.i * width + 25, self.j * height + 25, width, height))
		return


	def get_pals(self, parent_grid):
		pals = []
		# check for edge cases
		edge_left = self.i == 0
		edge_right = self.i + 1 == len(parent_grid)
		edge_up = self.j == 0
		edge_down = self.j + 1 == len(parent_grid)
		if not edge_left:
			pals.append(parent_grid[self.i - 1][self.j])
			if not edge_up:
				pals.append(parent_grid[self.i - 1][self.j - 1])
			if not edge_down:
				pals.append(parent_grid[self.i - 1][self.j + 1])
		if not edge_right:
			pals.append(parent_grid[self.i + 1][self.j])
			if not edge_up:
				pals.append(parent_grid[self.i + 1][self.j - 1])
			if not edge_down:
				pals.append(parent_grid[self.i + 1][self.j + 1])
		if not edge_up:
			pals.append(parent_grid[self.i][self.j - 1])
		if not edge_down:
			pals.append(parent_grid[self.i][self.j + 1])
		return pals