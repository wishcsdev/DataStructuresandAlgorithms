class Stack:
    def __init__(self, items=[]):
        self.items = items
 
    def push(self, item):
        self.items += [item]

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left, self.right = left, right

#precondition: tree != None
def o(tree, node):
    if node.data <= tree.data:						// if the data in the node is less than the data in the tree
        if tree.left == None: tree.left = node		// if left of the tree is empty then left of tree is the node. 
        else: insert(tree.left, node)				// run above again recursively on the left tree to insert at LEAF ALWAYS(property of BST)
    else:
        if tree.right == None: tree.right = node
        else: insert(tree.right, node)

def traverse_pre(tree):
    if tree==None: return
    print(tree.data, end=" ")
    traverse_pre(tree.left)							//recursively call left tree and print the data in the nodes.
    traverse_pre(tree.right)

def traverse_in(tree):
    if tree==None: return
    traverse_in(tree.left)
    print(tree.data, end=" ")
    traverse_in(tree.right)

def traverse_post(tree):
    if tree==None: return
    traverse_post(tree.left)
    traverse_post(tree.right)
    print(tree.data, end=" ")

# assume tree is a binary search tree
def get_max(tree):							//max of tree is on the right most node of the right side
    while tree.right != None: 				//
		tree = tree.right
    return tree.data

def get_min(tree):
    while tree.left != None: 				//vice versa for min
		tree = tree.left
    return tree.data

def visit(tree):
    if tree == None: 
		return 0, 0
    sum_left, count_left = visit(tree.left)
    sum_right, count_right = visit(tree.right)
    return sum_left + sum_right + tree.data, \
           count_left + count_right + 1

# this is interesting, recursion while accumulating a sum
def get_ave(tree):
    sum, count = visit(tree) 
    return float(sum)/count


def bfs(root):
    active = [root]												//root NODE is in the initialized active list
    while active != []:											//when active list is not empty
        for node in [active[0].left, active[0].right]:			//for the first nodes on the left and right side
            if node != None:									//while the node exists for  
				active += [node]								//add the node to the active list
        print(active[0].data)									//print the data in the first 
        active = active[1:]  

def dfs(root):
    traverse_pre(root)

def traverse_in_stack(tree):
    stack = Stack()
    while not (stack.is_empty() and tree == None):
        if tree != None:
            stack.push(tree)
            tree = tree.left
        else:
            tree = stack.pop()
            print(tree.data, end=" ")
            tree = tree.right
#    while tree != None:
#        stack.push(tree)
#        tree = tree.left
#    while not stack.is_empty():
#        node = stack.pop()
#        print(node.data, end = " ")
#        if node.right != None: 
#            p = node.right
#            while p != None: 
#                stack.push(p)
#                p = p.left

root = Node(60)
n1,n2,n3,n4,n5,n6,n7,n8 = Node(20),Node(10),Node(15),Node(30),Node(40),Node(5),Node(100),Node(200)
root.left,root.right = n1, n5
n1.left,n1.right = n2,n3
n3.left = n4
n5.right = n6
n6.left, n6.right = n7,n8

#traverse_pre(root)
#print()
traverse_in(root)
print()
#traverse_post(root)
#print()

#print(get_min(root))
#print(get_max(root))
#print(get_ave(root))

#bfs(root)
#dfs(root)

#print()
#traverse_in_stack(root)
#print()

#60 20 10 15 30 40 5 100 200
#10 20 30 15 60 40 100 5 200
#10 30 15 20 100 200 5 40 60
