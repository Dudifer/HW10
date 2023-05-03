#Algorithms HW 10
#do not include any print statements in your program
#your program should return the desired result
#there was a typographical error in the name of the 4th function
#it should be as it appears here

def getHawkID():
	hawkID = 'janyberg'
	return [hawkID]

def pathExists(A, vertex1, vertex2):
	paths=[vertex1]
	length=len(A[0])
	explored=0
	while explored<length:
		for cur_v in paths:
			for v in range(length):
				if A[cur_v][v]==1:
					if v==vertex2: return True
					elif v!=cur_v and v not in paths: paths.append(v)
			explored+=1		
	#could save lines by writing a second function 
	paths=[vertex2]
	explored=0
	while explored<length:
		for cur_v in paths:
			for v in range(length):
				if A[cur_v][v]==1:
					if v==vertex1: return True
					elif v!=cur_v and v not in paths: paths.append(v)
			explored+=1
	return False

def symmetricClosure(A):
	length=len(A[0])
	for v1 in range(length):
		for v2 in range(length):
			if v2==v1: continue
			elif A[v1][v2]==1:
				A[v2][v1]=1
	return A




def binaryStrings(n):
	A=['0','1']
	for a in range(1,n):
		A=[s+'1' for s in A]+[s+'0' for s in A if s[-1]!='0']
	A.sort()
	return A

