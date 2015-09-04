''' 
	Sam Skolnekovich
	3202 Assignment 1
	09/04/15
'''

''' 
	One problem in code. 
	
	Binary tree deletion is not correct. Seems to always think the the current node has children.
'''


import queue

class queball (queue.Queue):
	
	def __init__(self):
		queue.Queue.__init__(self)

	def put(self, value,*block,**timeout):
		if (isinstance(value,int)):
			queue.Queue.put(self,value,block,timeout)
		else:
			print("Unable to add, make sure you added an integer")

	def get(self,*block,**timeout):

		return queue.Queue.get(self)


class SingleStacker: # I assumed we could use methods in list data type.
	stacker=[] 
	def __init__(self):
		self.stacker=[]
		
	def push(self,value):
		self.stacker.append(value)
	
	def pop(self):
		self.stacker.pop()    
		
	
	def checksize(self):
		count=0
		for x in self.stacker:
			count=count+1;
		print(count)
			
	

class node:
	def __init__(self,leftnode, rightnode,nn_value,parent):
		self.leftnode=leftnode
		self.rightnode=rightnode
		self.nn_value=nn_value
		self.parent=parent

	def getleftnode(self):
		return self.leftnode
	def getrightnode(self):
		return self.rightnode
	def getvalue(self):
		return self.nn_value
	
	
	def setleftnode(self,leftnode):
		self.leftnode=leftnode
	def setrightnode(self,rightnode):
		self.rightnode=rightnode
	
	def printnodes(self):				# easier to call from node than in binary tree class
		print(self.nn_value)
		if(self.leftnode != None):
			self.leftnode.printnodes()
		if(self.rightnode!=None):
			self.rightnode.printnodes()      
		else:
			return
		

class binaryTree():
	
	def __init__(self,rootnode,allnodes):
		self.rootnode=rootnode
		self.allnodes=allnodes
		
	def add(self,value, parentvalue):
		
		for nodes in self.allnodes:
			if(nodes.getvalue()==parentvalue):
				newnode=node(None, None, value, nodes)
				if(nodes.getleftnode()==None):
					self.allnodes.append(newnode)
					nodes.setleftnode(newnode)
					return
			
				elif(nodes.getrightnode()==None):
					self.allnodes.append(newnode)
					nodes.setrightnode(newnode)
					return
				else:
					print ("parent already has two children")
					return
		print ("parent not found in tree")
	
	def delete(self, value):
		for nodes in self.allnodes:
			if(nodes.getvalue()==value):
				if(nodes.getrightnode != None or nodes.getleftnode != None): #error on this line 
					print ("parent cannot be deleted")
					return
				else:
					self.allnodes.remove(nodes)
					return
		
		print("Node not found")
	
	def print_it(self):
		self.rootnode.printnodes()
			
class graph():
	vertices={}
	def __init__(self):
		self.vertices={}
		
	def addVertex(self, value):
		if(value not in self.vertices):
			self.vertices[value]=[]
		else:
			print("vertex already exists")
	def addEdge(self,vertex1, vertex2):
		if(vertex1 not in self.vertices or vertex2 not in self.vertices):
			print ("one or more vertices not found")
		else:
			self.vertices[vertex1].append(vertex2)
			self.vertices[vertex2].append(vertex1)
		
	def findVertex(self,value):
		y=False						#boolean value turns true if found vertex and then use print outside loop
		for x in self.vertices:
		
			if (value==x):
				y=True
				
		if(y==True):
			print("vertex with value", value, "found", self.vertices[value])
		else:
			print("not found")








def testQueue():
	testQueue=queball()
	for x in range(1,16):
		testQueue.put(x)
	for x in range(1,16):				#deque and print ints
		print (testQueue.get())
		
def testStack():
	testStack=SingleStacker()
	
	for x in range(1,21):
		testStack.push(x)
	
	print(testStack.stacker)
	
	for x in range(1,21):
		size=testStack.checksize() 
		if size!=0:
			testStack.pop()

		
def testBinaryTree():
	test=node(None,None,1,None) #value set to one, everything else set null
	
	testBinaryTree=binaryTree(test,[test]) #binary tree with only a root node
	
	testBinaryTree.add(2,1)	#add 12 nodes
	testBinaryTree.add(3,1)
	testBinaryTree.add(4,2)	
	testBinaryTree.add(5,3)
	testBinaryTree.add(6,2)
	testBinaryTree.add(7,3)
	testBinaryTree.add(8,4)
	testBinaryTree.add(9,8)
	testBinaryTree.add(10,9)
	testBinaryTree.add(11,10)
	testBinaryTree.add(12,10)
	testBinaryTree.add(13,12)
	
	testBinaryTree.print_it()
	
	
	testBinaryTree.add(22,1)		#try to add a node to a parent with two children
	testBinaryTree.add(47,48) 		#try to add a node to unexistant parent
	testBinaryTree.delete(2)		#try to delete a node with children

	testBinaryTree.delete(1)		#deletion 
	testBinaryTree.delete(13)
	testBinaryTree.delete(8)
	
	testBinaryTree.print_it()   	#print w/ deletions
	


def testGraph():
	
	testGraph=graph()
	for x in range (1,11):
		testGraph.addVertex(10*x) 		#add vertices
		x=x+1
	
	testGraph.addEdge(10,30)			#add 20 edges
	testGraph.addEdge(10,40)
	testGraph.addEdge(10,50)
	testGraph.addEdge(20,30)
	testGraph.addEdge(30,90)
	testGraph.addEdge(20,10)
	testGraph.addEdge(80,90)
	testGraph.addEdge(70,90)
	testGraph.addEdge(40,30)
	testGraph.addEdge(50,60)
	testGraph.addEdge(60,70)
	testGraph.addEdge(60,80)
	testGraph.addEdge(70,80)
	testGraph.addEdge(80,90)
	testGraph.addEdge(60,100)
	testGraph.addEdge(50,100)
	testGraph.addEdge(20,100)
	testGraph.addEdge(10,100)
	testGraph.addEdge(80,100)
	testGraph.addEdge(30,100)
	
	print(testGraph.vertices)
	
	#find 5 vertices
	
	testGraph.findVertex(10)
	testGraph.findVertex(30)
	testGraph.findVertex(50)
	testGraph.findVertex(70)
	testGraph.findVertex(100)
	
	
	

def main():
	testQueue()
	print(" ")
	testStack()
	print(" ")
	testBinaryTree()
	print(" ")
	testGraph()

	
if  __name__ =='__main__':main()

	
