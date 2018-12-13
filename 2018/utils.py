class DLLNode:
	def __init__(self, val):
		self.val = val
		self.prev = None
		self.next = None

class DLL:
	def __init__(self):
		self.curr = DLLNode(0)
		self.curr.next = self.curr
		self.curr.prev = self.curr
		self.length = 1

	def insert(self, val):
		node = DLLNode(val)
		# one spot CW
		self.curr = self.curr.next
		# two spots CW
		orig_next = self.curr.next
		self.curr.next = node
		node.prev = self.curr
		orig_next.prev = node
		node.next = orig_next
		self.curr = node
		self.length += 1

	def remove(self, pos):
		while pos > 0:
			# move pos positions CCW
			self.curr = self.curr.prev
			pos -= 1
		to_remove = self.curr
		self.curr = self.curr.next
		to_remove.prev.next = self.curr
		self.curr.prev = to_remove.prev
		self.length -= 1
		return to_remove.val

class TreeNode:
	def __init__(self, id, values, children):
		self.id = id
		self.values = values
		self.children = children

class Tree:
	def __init__(self, root):
		self.root = root

	def insert(self, node_to_insert, location):
		location.children.append(node_to_insert)

def get_input_data(filename):
	f = open(filename, "r")
	items = []
	line = f.readline()
	while line:
		items.append(line)
		line = f.readline()
	f.close()
	return items

