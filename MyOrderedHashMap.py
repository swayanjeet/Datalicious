
class Node:
	"""
	This class is used for initializing the nodes of a tree
	"""
	def __init__(self, key, value, left = None, right = None):
		self.key = key
		self.value = value
		self.left = left
		self.right = right

class MyOrderedHashMap:
	"""
	This is the ordered hash map class
	"""
	def __init__(self):
		self.root = None

	def put(self, key, value):
		"""
		This puts a key and a value pair into the hashmap
		"""
		if self.root == None:
			self.root = Node(key, value)
		else:
			current = self.root
			parent = None
			pointer = None
			while current is not None:
				if current.key < key:
					parent = current
					current = current.right
					pointer = "right"
				else:
					parent = current
					current = current.left
					pointer = "left"
			current = Node(key, value)
			if pointer is "right":
				parent.right = current
			else:
				parent.left = current


	def inorder(self, root):
		"""
		This is used for in-order traversal of the tree
		"""
		if root is not None:
			self.inorder(root.left)
			print hash(root.key),
			self.inorder(root.right)

	def minValueNode(self,node):
		"""
		This is used for the finding the node with minimum value
		"""
		current = node
		parent = None
		while(current.left is not None): 
			parent = current
			current = current.left
		return current, parent

	def search(self,key):
		"""
		This is used for searching a node
		"""
		current = self.root
		while current.key != key:
			if current.key < key:
				current = current.right
			else:
				current = current.left
			if current is None:
				break
		if current is None:
			return "nf"
		else:
			return current

	def search_value(self,key):
		"""
		This is used for returning the value of a key
		"""
		current = self.root
		while current.key != key:
			if current.key < key:
				current = current.right
			else:
				current = current.left
			if current is None:
				break
		if current is None:
			return "nf"
		else:
			return current.value

	def delete(self,key):
		"""
		This is used for deleting the key and value
		"""
		current = self.root
		parent = None
		while current.key != key:
			if current.key < key:
				parent = current
				current = current.right
			else:
				parent = current
				current = current.left

		if current.right is None and current.left is None:
			if parent.right is current:
				parent.right = None
			else:
				parent.left = None
			current = None
		elif current.right is not None and current.left is None:
			if parent.right is current:
				parent.right = current.right
				current = None
			elif parent.left is current:
				parent.left = current.right
				current = None
		elif current.left is not None and current.right is None:
			if parent.left is current:
				parent.left = current.left
				current = None
			elif parent.right is current:
				parent.right = current.left
				current = None
		elif current.left is not None and current.right is not None:
			temp, temp_parent = self.minValueNode(current)
			current.key = temp.key
			current.value = temp.value
			temp_parent.left = None


# map1 = MyOrderedHashMap()
# map1.put(hash("key"),"key")
# map1.put(30, "key1")
# map1.put(20, "key3")
# map1.put(40, "key3")
# map1.put(60, "key3")
# map1.put(70, "key3")
# map1.put(80, "key3")
# map1.inorder(map1.root)
# map1.delete(20)
# map1.inorder(map1.root)
# print map1.search_value(hash("key"))
# print map1.search(hash("key4"))
# print map1.delete(hash("key3"))
# print map1.search_value(hash("key3"))
