def getHawkID():
     myID = 'janyberg'
     return [myID]
def findSources(V, E):
	potentialSrc=V
	for t in E:
		if t[1] in potentialSrc:
			potentialSrc.remove(t[1])
	return potentialSrc
def amITopological(M, L):
    covered=[]
    length=len(M[0])
    if len(L) != length:
        return False
    for v in L:
        for r in range(length):
            if M[r][v]==1 and r not in covered and r!=v:
                return False
        covered.append(v)
    return True
