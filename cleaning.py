import re
expr = " [ ]*"
f = open('housing.csv','r')
fwr = open('housingClean.csv','w')
for line in f.readlines():
    pattern = re.compile(expr)
    x = re.split(pattern, line)
    #x[-1] = x[-1].replace('\n','')
    x = ','.join(x)
    #print(x)
    fwr.write(x)
f.close()
fwr.close()

fwr = open('housingClean.csv', 'r')

i=0
for line in fwr.readlines():
    if len(line.split(',')) != 14:
        print(line.split(','))
        print("ABORT")
        print(i)
        break
    i+=1
fwr.close()