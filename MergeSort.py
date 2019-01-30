def merge_sort(A,B):
	C=[]				
	while A or B:
		C.append(min(A[0],B[0]))                  #C = 10, 44, 22, 65, 200,1001
		if A[0]<=B[0]:
			A=A[1:]
		else:
			B=B[1:]		
	return C+A+B

def Merge(A):
	length=len(A)
	
	if length<1:
		return A
		
	middle=(length)//2
	return merge_sort(A[:middle],A[middle:])


	
A=[10,200,1001,44,22,65]
A = Merge(A)
print(A)
