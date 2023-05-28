numlist = []

while True :
    inp = input('Enter a number: ')
    if inp == 'done' :
        print('done')
        break
    try :
        num = float(inp)
    except :
        print('Please enter a numeric value')
        continue
    numlist.append(num)

try :
    maxnum = max(numlist)
    minmum = min(numlist)
    print(f'Maximum: {maxnum}\nMinimum: {minmum}')
except :
    print('No values provided')
    exit()