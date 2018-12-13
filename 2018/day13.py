from utils import get_input_data

# Paths
H_PATH = "-"
V_PATH = "|"
BACK_CURVE = "\\"
FWD_CURVE = "/"
INTERSECTION = "+"
PATH_OBJECTS = set([H_PATH, V_PATH, BACK_CURVE, FWD_CURVE, INTERSECTION])

CARTS = {"<":H_PATH, ">":H_PATH, "^":V_PATH, "v":V_PATH}

# Moves
INIT = "initial"
LEFT = "left"
RIGHT = "right"
STRAIGHT = "straight"
NEXT_TURN = {INIT: LEFT, LEFT: STRAIGHT, STRAIGHT:RIGHT, RIGHT: LEFT}

class Grid:
	grid = None
	num_rows = 0
	num_cols = 0
	next_cart_id = 97
	carts = {}
	collision = None
	removed_carts = set()
	last_cart = None
	def __init__(self, input_grid):
		self.grid = [list(row) for row in input_grid]
		self.num_rows = len(input_grid)
		self.num_cols = len(input_grid[0])
		for row in xrange(self.num_rows):
			for col in xrange(self.num_cols):
				if self.grid[row][col] in CARTS:
					cart_id = chr(self.next_cart_id)
					new_cart = Cart(cart_id, col, row, self.grid[row][col])
					self.carts[cart_id] = new_cart
					self.grid[row][col] = cart_id
					self.next_cart_id += 1

	def get_left(self, x, y):
		return self.grid[y][x-1]

	def get_right(self, x, y):
		return self.grid[y][x+1]

	def get_up(self, x, y):
		return self.grid[y-1][x]

	def get_down(self, x, y):
		return self.grid[y+1][x]

	def print_grid(self):
		for row in self.grid:
			print("".join(row))

	def get_carts(self):
		cart_ids = []
		for row in xrange(self.num_rows):
			for col in xrange(self.num_cols):
				if self.grid[row][col] in self.carts:
					cart_ids.append(self.grid[row][col])
		return cart_ids

	def next_tick(self):
		cart_ids = self.get_carts()
		if len(cart_ids) == 11:
			print('11')
		elif len(cart_ids) == 7:
			print('7')	
		elif len(cart_ids) == 1:
			grid.last_cart = grid.carts[cart_ids[0]]
			return
		for cart_id in cart_ids:
			cart = self.carts[cart_id]
			cart.move(self)

class Cart:

	def __init__(self, cart_id, x, y, orientation):
		self.id = cart_id
		self.x = x
		self.y = y
		self.o = orientation
		self.tile = CARTS[orientation]
		self.next_turn = NEXT_TURN[INIT]

	def turn(self, direction):
		if direction == STRAIGHT:
			# TODO: handle +/ and the like
			return

		if self.o == ">":
			if direction == LEFT:
				self.o = "^"
			elif direction == RIGHT:
				self.o = "v"

		elif self.o == "<":
			if direction == LEFT:
				self.o = "v"
			elif direction == RIGHT:
				self.o = "^"

		elif self.o == "^":
			if direction == LEFT:
				self.o = "<"
			elif direction == RIGHT:
				self.o = ">"

		else: #"v"
			if direction == LEFT:
				self.o = ">"
			elif direction == RIGHT:
				self.o = "<"

	def move_left(self, next_tile, grid):
		grid[self.y][self.x] = self.tile
		self.tile = next_tile
		self.x -= 1
		grid[self.y][self.x] = self.id

	def move_right(self, next_tile, grid):
		grid[self.y][self.x] = self.tile
		self.tile = next_tile
		self.x += 1
		grid[self.y][self.x] = self.id

	def move_up(self, next_tile, grid):
		grid[self.y][self.x] = self.tile
		self.tile = next_tile
		self.y -= 1
		grid[self.y][self.x] = self.id

	def move_down(self, next_tile, grid):
		grid[self.y][self.x] = self.tile
		self.tile = next_tile
		self.y += 1
		grid[self.y][self.x] = self.id

	def process_h_move(self, next_tile):
		if next_tile == FWD_CURVE:
			self.turn(LEFT)
		elif next_tile == BACK_CURVE:
			self.turn(RIGHT)
		elif next_tile == INTERSECTION:
			self.turn(self.next_turn)
			self.next_turn = NEXT_TURN[self.next_turn]

	def process_v_move(self, next_tile):
		if next_tile == FWD_CURVE:
			self.turn(RIGHT)
		elif next_tile == BACK_CURVE:
			self.turn(LEFT)
		elif next_tile == INTERSECTION:
			self.turn(self.next_turn)
			self.next_turn = NEXT_TURN[self.next_turn]

	def move(self, grid):
		if self.id in grid.removed_carts:
			return
		if self.o == "<":
			left = grid.get_left(self.x, self.y)
			if not left in PATH_OBJECTS:
				grid.collision = (self.x-1, self.y)
				self.id = grid.carts[left].tile
				grid.removed_carts.add(self.id)
				grid.removed_carts.add(left)
			self.process_h_move(left)
			self.move_left(left, grid.grid)

		elif self.o == ">":
			right = grid.get_right(self.x, self.y)
			if not right in PATH_OBJECTS:
				grid.collision = (self.x+1, self.y)
				self.id = grid.carts[right].tile
				grid.removed_carts.add(self.id)
				grid.removed_carts.add(right)				
			self.process_h_move(right)
			self.move_right(right, grid.grid)

		elif self.o == "^":
			up = grid.get_up(self.x, self.y)
			if not up in PATH_OBJECTS:
				grid.collision = (self.x, self.y-1)	
				self.id = grid.carts[up].tile
				grid.removed_carts.add(self.id)
				grid.removed_carts.add(up)				
			self.process_v_move(up)
			self.move_up(up, grid.grid)

		else:
			down = grid.get_down(self.x, self.y)
			if not down in PATH_OBJECTS:
				grid.collision = (self.x, self.y+1)
				self.id = grid.carts[down].tile
				grid.removed_carts.add(self.id)
				grid.removed_carts.add(down)				
			self.process_v_move(down)
			self.move_down(down, grid.grid)		


if __name__ == "__main__":
	data = get_input_data("day13input.txt")
	grid = Grid(data)
	# part 1
	while grid.collision == None:
		grid.next_tick()
	grid.print_grid()
	print(grid.collision)

	#part 2
	while grid.last_cart == None:
		grid.next_tick()
	grid.print_grid()
	print(grid.last_cart.x, grid.last_cart.y)