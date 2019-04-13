class Graph(object):
    def __init__(self, edges, count):
    	self.edges = edges
    	self.count = count

class Edge(object):
	def __init__(self, node1, node2, cost):
		self.node1 = node1
		self.node2 = node2
		self.cost = cost
	def __lt__(self, other):
		return self.cost < other.cost
	def __str__(self):
		return str(self.node1) + ' ' + str(self.node2)

def read_file(path):
	edges = []
	y = 0
	with open(path, "r") as file:
		for line in file.readlines():
			x = 0
			for cost in line.split():
				if int(cost) is not 0:
					edges.append(Edge(y, x, int(cost)))
				x += 1
			y += 1
	edges.sort()
	return Graph(edges, y)
