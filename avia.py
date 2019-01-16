import sys
from itertools import islice


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


def zipzip(a, b):
    o = []
    for i in range(int(len(a))):
        left = a[i]
        right = b[i]
        if left == right:
            c = left
        else:
            c = left + '-' + right
        o.append(c)
    return o


def list_of_flights(a, b):
    with open('flights.av') as f:
        file = f.read().splitlines()
    keys = [' ', 'from', 'to', 'dep', 'arr', 'cost', 'airlines']
    flight = list(chunk(file, 7))
    flights = []
    for i in range(0, int(len(file)/7)):
        flights.append(dict(zip(keys, flight[i])))

    final = []
    one = []
    two = []

    direct_flights = [f for f in flights if a in f['from'] and b in f['to']]

    first_segment = [f for f in flights if a in f['from']]
    second_segment = [f for f in flights if b in f['to']]

    flights_w_1stop = []
    for s1 in first_segment:
        for s2 in second_segment:
            if (s1['to'][4:] == s2['from'][6:] and
                s1['arr'] < s2['dep']):
                flights_w_1stop.append((s1, s2))

    first_segment = [f for f in flights if a in f['from']]
    second_segment = [f for f in flights]
    third_segment = [f for f in flights if b in f['to']]

    flights_w_2stops = []
    for s1 in first_segment:
        for s2 in second_segment:
            for s3 in third_segment:
                if (s1['to'][4:] == s2['from'][6:] and
                    s2['to'][4:] == s3['from'][6:] and
                    s1['arr'] < s2['dep'] and
                    s2['arr'] < s3['dep']):
                    flights_w_2stops.append((s1, s2, s3))
    for i in direct_flights:
        time1 = i['arr'][9:]
        time2 = i['dep'][11:]
        time = (float(time1[0:2])/10 - float(time2[0:2])/10)*600 + float(time1[3:5]) - float(time2[3:5])/60
        final.append(i['from'][6:] + ' ' + i['dep'][11:] + ' -> ' + i['to'][4:] + ' ' + i['arr'][9:] + ' ' + str(time) + 'min ' + i['cost'][6:])
        final.sort()

    times1 = []
    t1 = []
    prices1 = []
    p1 = []
    airline1 = []
    a1 = []
    a2 = []
    o1 = []
    for j in flights_w_1stop:
        for i in j:
            time1 = i['arr'][9:]
            time2 = i['dep'][11:]
            time = (float(time1[0:2])/10 - float(time2[0:2])/10)*600 + float(time1[3:5]) - float(time2[3:5])/60
            one.append(i['from'][6:] + ' ' + i['dep'][11:] + ' -> ' + i['to'][4:] + ' ' + i['arr'][9:] + ' ' + str(round(float(time)/60, 1)) + ' ' + i['cost'][6:] + ' ' + i['airlines'][10:])
    newlist = [word for line in one for word in line.split()]
    for i in range(5, int(len(newlist)), 8):
        times1.append(newlist[i])
    for i in range(0, int(len(times1)), 2):
        t1.append(int(float(times1[i]) + float(times1[i + 1])))
    for i in range(6, int(len(newlist)), 8):
        prices1.append(newlist[i])
    for i in range(0, int(len(prices1)), 2):
        p1.append(str(int(prices1[i][1:]) + int(prices1[i+1][1:])))
    for i in range(7, int(len(newlist)), 8):
        airline1.append(newlist[i])
    for i in range(0, int(len(airline1)), 2):
        a1.append(airline1[i])
        a2.append(airline1[i+1])
    o1 = zipzip(a1, a2)
    one1 = list(zip(o1, t1, p1, list(chunk(one, 2))))
    one1.sort()

    times2 = []
    t2 = []
    prices2 = []
    p2 = []
    airline2 = []
    a3 = []
    a4 = []
    o2 = []
    if len(flights_w_2stops) > 1:
        for j in flights_w_2stops:
            for i in j:
                time1 = i['arr'][9:]
                time2 = i['dep'][11:]
                time = (float(time1[0:2])/10 - float(time2[0:2])/10)*600 + float(time1[3:5]) - float(time2[3:5])/60
                two.append(i['from'][6:] + ' ' + i['dep'][11:] + ' -> ' + i['to'][4:] + ' ' + i['arr'][9:] + ' ' + str(round(float(time)/60, 1)) + ' ' + i['cost'][6:] + ' ' + i['airlines'][10:])
        newlist = [word for line in two for word in line.split()]
        for i in range(5, int(len(newlist)), 8):
            times2.append(newlist[i])
        for i in range(0, int(len(times2)), 2):
            t2.append(int(float(times2[i]) + float(times2[i+1])))
        for i in range(6, int(len(newlist)), 8):
            prices2.append(newlist[i])
        for i in range(0, int(len(prices2)), 2):
            p2.append(str(int(prices2[i][1:]) + int(prices2[i+1][1:])))
        for i in range(7, int(len(newlist)), 8):
            airline2.append(newlist[i])
        for i in range(0, int(len(airline1)), 2):
            a3.append(airline2[i])
            a4.append(airline2[i+1])
            o2 = zipzip(a3, a4)
    elif len(flights_w_2stops) == 1:
        for j in flights_w_2stops:
            for i in j:
                time1 = i['arr'][9:]
                time2 = i['dep'][11:]
                time = (float(time1[0:2])/10 - float(time2[0:2])/10)*600 + float(time1[3:5]) - float(time2[3:5])/60
                two.append(i['from'][6:] + ' ' + i['dep'][11:] + ' -> ' + i['to'][4:] + ' ' + i['arr'][9:] + ' ' + str(round(float(time)/60, 1)) + ' ' + i['cost'][6:] + ' ' + i['airlines'][10:])
        newlist = [word for line in two for word in line.split()]
        for i in range(int(len(newlist))):
            t2.append(newlist[5])
            p2.append(newlist[6])
            o2.append(newlist[7])
    two1 = list(zip(o2, t2, p2, list(chunk(two, 3))))
    two1.sort()
    jesus = one1 + two1
    jesus.sort()
    return final, jesus


def list_of_cheap_flights(a, b):
    with open('flights.av') as f:
        file = f.read().splitlines()
    keys = [' ', 'from', 'to', 'dep', 'arr', 'cost', 'airlines']
    flight = list(chunk(file, 7))
    flights = []
    for i in range(0, int(len(file)/7)):
        flights.append(dict(zip(keys, flight[i])))

    final = []
    one = []
    two = []

    direct_flights = [f for f in flights if a in f['from'] and b in f['to']]

    first_segment = [f for f in flights if a in f['from']]
    second_segment = [f for f in flights if b in f['to']]

    flights_w_1stop = []
    for s1 in first_segment:
        for s2 in second_segment:
            if (s1['to'][4:] == s2['from'][6:] and
                s1['arr'] < s2['dep']):
                flights_w_1stop.append((s1, s2))

    first_segment = [f for f in flights if a in f['from']]
    second_segment = [f for f in flights]
    third_segment = [f for f in flights if b in f['to']]

    flights_w_2stops = []
    for s1 in first_segment:
        for s2 in second_segment:
            for s3 in third_segment:
                if (s1['to'][4:] == s2['from'][6:] and
                    s2['to'][4:] == s3['from'][6:] and
                    s1['arr'] < s2['dep'] and
                    s2['arr'] < s3['dep']):
                    flights_w_2stops.append((s1, s2, s3))

    for i in direct_flights:
        time1 = i['arr'][9:]
        time2 = i['dep'][11:]
        time = (float(time1[0:2])/10 - float(time2[0:2])/10)*600 + float(time1[3:5]) - float(time2[3:5])/60
        final.append(i['cost'][7:] + ' ' + str(round(float(time)/60, 1)) + ' ' + i['from'][6:] + ' -> ' + i['to'][4:])
        final.sort()

    times1 = []
    t1 = []
    prices1 = []
    p1 = []
    airline1 = []
    a1 = []
    a2 = []
    o1 = []
    for j in flights_w_1stop:
        for i in j:
            time1 = i['arr'][9:]
            time2 = i['dep'][11:]
            time = (float(time1[0:2])/10 - float(time2[0:2])/10)*600 + float(time1[3:5]) - float(time2[3:5])/60
            one.append(i['from'][6:] + ' ' + i['dep'][11:] + ' -> ' + i['to'][4:] + ' ' + i['arr'][9:] + ' ' + str(round(float(time)/60, 1)) + ' ' + i['cost'][6:] + ' ' + i['airlines'][10:])
    newlist = [word for line in one for word in line.split()]
    for i in range(5, int(len(newlist)), 8):
        times1.append(newlist[i])
    for i in range(0, int(len(times1)), 2):
        t1.append(int(float(times1[i]) + float(times1[i + 1])))
    for i in range(6, int(len(newlist)), 8):
        prices1.append(newlist[i])
    for i in range(0, int(len(prices1)), 2):
        p1.append(str(int(prices1[i][1:]) + int(prices1[i+1][1:])))
    for i in range(7, int(len(newlist)), 8):
        airline1.append(newlist[i])
    for i in range(0, int(len(airline1)), 2):
        a1.append(airline1[i])
        a2.append(airline1[i+1])
    o1 = zipzip(a1, a2)
    one1 = list(zip(p1, o1, list(chunk(one, 2)), t1))
    one1.sort()

    times2 = []
    t2 = []
    prices2 = []
    p2 = []
    airline2 = []
    a3 = []
    a4 = []
    o2 = []
    if len(flights_w_2stops) > 1:
        for j in flights_w_2stops:
            for i in j:
                time1 = i['arr'][9:]
                time2 = i['dep'][11:]
                time = (float(time1[0:2])/10 - float(time2[0:2])/10)*600 + float(time1[3:5]) - float(time2[3:5])/60
                two.append(i['from'][6:] + ' ' + i['dep'][11:] + ' -> ' + i['to'][4:] + ' ' + i['arr'][9:] + ' ' + str(round(float(time)/60, 1)) + ' ' + i['cost'][6:] + ' ' + i['airlines'][10:])
        newlist = [word for line in two for word in line.split()]
        for i in range(5, int(len(newlist)), 8):
            times2.append(newlist[i])
        for i in range(0, int(len(times2)), 2):
            t2.append(int(float(times2[i]) + float(times2[i+1])))
        for i in range(6, int(len(newlist)), 8):
            prices2.append(newlist[i])
        for i in range(0, int(len(prices2)), 2):
            p2.append(str(int(prices2[i][1:]) + int(prices2[i+1][1:])))
        for i in range(7, int(len(newlist)), 8):
            airline2.append(newlist[i])
        for i in range(0, int(len(airline1)), 2):
            a3.append(airline2[i])
            a4.append(airline2[i+1])
            o2 = zipzip(a3, a4)
    elif len(flights_w_2stops) == 1:
        for j in flights_w_2stops:
            for i in j:
                time1 = i['arr'][9:]
                time2 = i['dep'][11:]
                time = (float(time1[0:2])/10 - float(time2[0:2])/10)*600 + float(time1[3:5]) - float(time2[3:5])/60
                two.append(i['from'][6:] + ' ' + i['dep'][11:] + ' -> ' + i['to'][4:] + ' ' + i['arr'][9:] + ' ' + str(round(float(time)/60, 1)) + ' ' + i['cost'][6:] + ' ' + i['airlines'][10:])
        newlist = [word for line in two for word in line.split()]
        for i in range(int(len(newlist))):
            t2.append(newlist[5])
            p2.append(newlist[6])
            o2.append(newlist[7])
    two1 = list(zip(p2, o2, list(chunk(two, 3)), t2))
    two1.sort()
    jes = one1 + two1
    jes.append(tuple(final))
    jes.sort()
    return jes


arg = sys.argv
try:
    if arg[1] == 'add':
        f = open('flights.av', 'a+')
        f.write('From: ' + arg[2])
        f.write('\nTo: ' + arg[3])
        f.write('\nDeparture: ' + arg[4])
        f.write('\nArrival: ' + arg[5])
        f.write('\nCost: $' + arg[6])
        f.write('\nAirlines: ' + arg[7])
        f.write('\n\n')
        f.close()
    elif arg[1] == 'top':
        output = list_of_flights(arg[2], arg[3])
        if output is None:
            print('Unfortunately, there are no such flights!')
        else:
            print(output[0])
            if arg[4]:
                for i in range(1, int(arg[4])):
                    print(output[i])
    elif arg[1] == 'find-cheap':
        output = list_of_cheap_flights(arg[2], arg[3])
        if output is None:
            print('Unfortunately, there are no such flights!')
        else:
            print(output[0])
            if arg[4]:
                for i in range(1, int(arg[4])):
                    print(output[i])
except IndexError:
    pass
