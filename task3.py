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

    

        
        
    
    

    
    
