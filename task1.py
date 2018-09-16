def unique(e):
    a = []
    for i in e:
        if i not in a:
            a.append(i)
            a.sort()
        else:
            print ('Here is your sortet list of distinct elements!')
            return a
            
