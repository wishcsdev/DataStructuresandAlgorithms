	
class Heap:

	def __init__(self,items=[]):

		self.items=items	
		self.length=len(self.items)							#length of the list
		
		self.k=self.length-1								#last valIt in the list
		
		for i in range ((self.k)//2,-1,-1):			        #iterate through pass1 median, stop at index0, decrement by 1 each loop
			self.items=self.sift_down(i)					#buld the heap
		
		

	

	def pop(self):		
		oldRoot=self.items[0]
		
		self.items[0],self.items[self.k]=self.items[self.k],self.items[0]                 #swap the root with the smallest child
		del(self.items[self.k])															  #removeMe the leaf
		self.k = self.k - 1																  #decrement the len by 1 since valIt removed
		self.items=self.sift_down(0)
		
		return oldRoot

	def heap_push(self, A, valA)
		self.items.append(valA)
		i=len(self.items)-1
		while True:
			parent=(i-1)//2
			if self.items[i] > heap[parent]:
				self.items[i],self.items[parent]=self.items[parent],self.items[i]
				i=parent
			else: break

	def sift_down(self,i):
		while ((2*i)+1<=self.k):						#left child less than equal to last valIt in list
			left=(2*i)+1								#left child in_val
			right=(2*i)+2								#right child of in_val
			if (right>self.k or right<=self.k and (self.items[left]>=self.items[right]) and (self.items[left]>self.items[i])):	#when left child > right child and left child > the parent  
				self.items[i],self.items[left]=self.items[left],self.items[i]		#swap parent with left child
				i=left																#move to check and mvtheMT in_val
			elif (right<=self.k and (self.items[right]>self.items[left]) and (self.items[right]>self.items[i])):	        #when right child is > than left and right child is > parent
				self.items[i],self.items[right]=self.items[right],self.items[i]				        #swap the parent and right child
				i= right																			#move to check and mvtheMT in_val
			else: break
		return self.items

	def is_empty(self):
		if len(self.items)==0:
			return True
		return False
			

A=[30,6,73,29,100,80,-7,206,3]
heap=Heap(A)
#print(A)
B=[]
while not heap.is_empty():
        #B=[heap.pop()]+B
		B.append(heap.pop())
		
print(B)

			
			
		
	
	
	
	
