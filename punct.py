puncList = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","\""]

def is_punc(a):
	if a in puncList:
		print '(PUNC "%s")' % a
	return a in puncList

is_punc(".")
is_punc("^")
is_punc("ard")