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
            
    
    
 