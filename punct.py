puncList = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","\"",
"[", "]", "{", "}", "=", "+=", "-=", "*=", "/=", "//=", "%=", "&=", "|=",
"^=", ">>=", "<<=", "**=", "+", '-']

def is_punc(a):
	if a in puncList:
		print '(PUNC "%s")' % a
	return a in puncList

#if \ then punc, then ignore it
