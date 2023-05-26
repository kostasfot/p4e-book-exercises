fname = input('Enter file path: ')

try :
    if fname == 'na na boo boo' :
        print("'NA NA BOO BOO TO YOU - You have been punk'd!")
    fhand = open(fname)
    
except :
    print(f'File {fname}, not found')
    print('Setting path to exercise-files\mbox-short.txt')
    fname = 'exercise-files\mbox-short.txt'
    fhand = open(fname) 
    
count = 0
dsum = 0

for line in fhand :
    if not line.startswith('X-DSPAM-Confidence:') :
        continue
    colpos = line.find(':')
    dspam = float(line[colpos + 1:])
    count = count + 1
    dsum = dsum + dspam

print(f'Average spam confidence: {dsum/count}')