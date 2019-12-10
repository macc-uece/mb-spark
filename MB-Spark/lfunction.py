import sys
import re



def mstos(x):
    val = x/1000
    return val
      
def ustos(x):
    val = x/1000000
    return val
       
def nstos(x):
    val = x/1000000000
    return val

def convert(x,y):
    if y == 'ms':
        return mstos(x)
    elif y == 'µs':
        return ustos(x)
    elif y == 'ns':
        return nstos(x)
    else:
        return x    

    
def tratamento(k):
    
    try:
        x = convert(float(k.split(' ')[0]),k.split(' ')[1])
        y = convert(float(k.split(' ')[3]), k.split(' ')[4])
    except:
        p = re.findall(r"[-+]?\d*\.\d+|\d+", k)
        x = (float(p[0])*60) + float(p[1])
        y = convert(float(k.split(' ')[3]), k.split(' ')[4])

    return x, y
    
    
def duplicate(y, x, npath, lpath):
    npath = str(y) + str(x) + npath
    fout=open(npath,"a")
    for num in range(1,x):
        for line in open(lpath):
            fout.write(line)    
    fout.close()
    return npath
    
    