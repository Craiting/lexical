import re
from punct import is_punc
from keywords import is_keyword
from ID import is_ID


myfile = raw_input()

fin = open(myfile, 'r')

lines = fin.readlines()

def breakup_line(line):
    words = line.split()
    for i in range(len(words)):
        if words[i][0] in ("'",'"') and words[i][-1] in ("'",'"'): # don't break strings
            pass
        else: # break up further based on punctuation
            print 'w', words[i]
            t = re.findall(r"[\w]+|[^\s\w]|[-:\w]", words[i])
            print 't', t
            if len(t) > 1:
                words.remove(words[i])
                words[i:i] = t
    return words
            
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
            
            
            

for line in lines:
    tokens = breakup_line(line)
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
