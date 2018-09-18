def unique(e):
    a = []
    for i in e:
        if i not in a:
            a.append(i)
            a.sort()
    return a

            
            
def transposeDict(d):
    a = d.keys()
    b = d.values()
    new = dict(zip(b,a))   
   
    return new
    
    

def mex(e):
    k=1
    while k in e:
        k+=1
    else:
        return (k)
        
        
def frequencyDict(s):
    a = []
    b =[]
    for i in s:
        if i not in a:
            a.append(i)
    for j in a:
        c = s.count(j)
        b.append(c)
    new = dict(zip(a,b))
    return new    
