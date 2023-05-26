total = 0
count = 0
mnm = None
mxm = None

while True :
    num = input('Enter a number:')
    
    if num == 'done' :
        break
    try :
        num = float(num)
    except :
        print('Enter numeric input')
        continue
    
    if mnm == None or num < mnm :
        mnm = num
    
    if mxm == None or num > mxm :
        mxm = num
    
    total = total + num
    count = count + 1
    
print('Total:', total)
print('Count:', count)
print('Minimum:', mnm)
print('Maximum:', mxm)