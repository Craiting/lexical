import re
from punct import is_punc
from punct import puncList
from keywords import is_keyword
from ID import is_ID


myfile = raw_input()

fin = open(myfile, 'r')

lines = fin.readlines()

def breakup_line(line):
    words = line.split()
    newwords = []
    for i in range(len(words)):
        if words[i][0] in ("'",'"') and words[i][-1] in ("'",'"'): # don't break strings
            newwords.append(words[i])
        else: # break up further based on punctuation
            t = re.findall(r"[\w]+|[^\s\w]|[-:\w]", words[i])
            newwords.extend(t)
    return newwords
            
def get_strings(words):
    new_words = []
    adding = False
    tmpstring = ''
    skip = False
    for w in words:
        if w in ("'",'"'):
            adding = True
        elif w[-1] in ('"',"'"):
            adding = False
            tmpstring += w + ' '
            new_words.append(tmpstring)
            tmpstring = ''
            skip = True
        if adding:
            tmpstring += w + ' '
        else:
            if skip:
                skip = False
            else:
                new_words.append(w)
    return new_words
            
def get_double_punc(words):
    new_punc = []
    adding = False
    tmpstring = ''
    size = len(words)

    skip = False
    for w in words:
        if w in puncList and w < size+1:   
            while w[+1] in puncList:
                new_punc.append(w[+1])
                w=w+1
        else:
            new_punc.append(w)
    return new_punc
            

for line in lines:
    tokens = breakup_line(line)
    punc = get_double_punc(tokens)
    final = get_strings(tokens)
    for item in final:
        if is_punc(item):
            pass
        elif is_keyword(item):
            pass
        elif is_ID(item):
            pass
        else:
            print "(LIT %s)" % item
print "(ENDMARKER)"
