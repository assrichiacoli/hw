def unique(e):
    a = []
    for i in e:
        if i not in a:
            a.append(i)
            a.sort()
        else:
            print ('Here is your sortet list of distinct elements!')
            return a

            
            
def transposeDict(d):
    a = d.keys()
    b = d.values()
    new = dict(zip(a,b))   
   
    return new
    
    

def mex(e):
    a = []
    for i in e:
        try:
            a.append(int(i))
        except ValueError:
            continue
        a.sort()
    k=1
    while k in a:
        k+=1
    else:
        print (k)
        
        
def frequencyDict(s):
    a = []
    b =[]
    for i in s:
        if i not in a:
            a.append(i)
#        else:
#            print ('I counted all the symbols!')
    for j in a:
        c = s.count(j)
        b.append(c)
    new = dict(zip(a,b))
    return new    