import string

fname = input("Enter file name: ")

try :
    fhand = open(fname)
except :
    print("File cannot be opened:", fname)
    print('Setting file to mbox-short.txt')
    fhand = open('exercise-files/mbox-short.txt')

counts = dict()
    
atpos = None
domain = None
    
for line in fhand :
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From' : 
        continue
    atpos = words[1].find('@')
    domain = words[1][atpos+1 :]
    
    if domain not in counts :
        counts[domain] = 1
    else:
        counts[domain] += 1
        
print(counts)
    
mxkey = None
mxcnt = None
    
for key in counts :
    if mxcnt is None or counts[key] > mxcnt :
        mxcnt = counts[key]
        mxkey = key
        
print(mxkey, mxcnt)