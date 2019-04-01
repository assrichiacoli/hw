import sys
from collections import defaultdict, namedtuple, Counter
from itertools import chain, product, tee
import datetime

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


class Avia:
    Flight = namedtuple('Flight', 'From To Departure Arrival Cost Airlines Time')

    def __init__(self, flights=[]):
        self._airports = {}
        for flight in flights:
            flight = self.Flight(**flight)
            self[flight.From].add_flight(flight.To, flight)


    def __getitem__(self, key):
        try:
            return self._airports[key]
        except KeyError:
            ret = self._airports[key] = self.DepAirport(self, key)
            return ret


    class DepAirport:
        def __init__(self, graph, name):
            self._graph = graph
            self.name = name
            self._flights = defaultdict(set)


        def add_flight(self, airport, flight):
            self._graph[airport]
            self._flights[airport].add(flight)


        def flights(self, airport):
            if airport in self._flights:
                return frozenset(self._flights[airport])


        def _routes(self, destination, depth=1):
            depth += 1
            l = [[self.name]]
            while l:
                route = l.pop()
                name = route[-1]
                if name == destination:
                    yield route
                if len(route) == depth:
                    continue
                l.extend([(route + [a]) for a in self._graph[name]._flights.keys()])


        def routes(self, destination, depth=1):
            root = self._graph
            return chain.from_iterable(
                product(*(root[From].flights(To) for From, To in pairwise(route))) for route in self._routes(destination, depth))


def get(file):
    data = []
    current = {}
    with open(file) as f:
        for line in f:
            pair = line.split(': ', 1)
            if len(pair) == 2:
                if pair[0] == 'From' and current:
                    data.append(current)
                    current = {}
                current[pair[0]] = pair[1].rstrip()
        if current:
            data.append(current)
    return data


def calculate_time(flight):
    arr_ = datetime.datetime.strptime(flight['Arrival'], '%H:%M')
    dep_ = datetime.datetime.strptime(flight['Departure'], '%H:%M')
    time = ':'.join(str(abs(arr_ - dep_)).split(':')[:2])
    return time


def flights_with_time():
    fwt = []
    for i in get(file):
        i.update({'Time': calculate_time(i)})
        fwt.append(i)
    return fwt


def time_between_transfers(arrival,departure):
    origin = datetime.datetime(1900, 1, 1, 0, 0)
    arr_ = datetime.datetime.strptime(arrival, '%H:%M')
    dep_ = datetime.datetime.strptime(departure, '%H:%M')
    difference = abs(dep_ - arr_) + origin
    return difference


def check_40_mins(arrival,departure):
    origin = datetime.datetime(1900, 1, 1, 0, 0)
    fortymin = datetime.datetime(1900, 1, 1, 0, 40)
    day = datetime.datetime(1900, 1, 1, 23, 0)
    if time_between_transfers(arrival,departure) > fortymin and time_between_transfers(arrival,departure) > origin\
        and time_between_transfers(arrival,departure) <= day:
        return True
    else:
        return False


def calculate_cost(flight_):
    for i in flight_:
        return sum(int(i.cost[1:]))


def airlines_change(flight):
    airlines = [route.Airlines for route in flight]
    return Counter(airlines).values()


def total_cost(flight):
    costs = [(int(route.Cost[1:])) for route in flight]
    return sum(costs)


def total_time(flight):
    return time_between_transfers(flight[0].Arrival, flight[-1].Departure)


file = 'flights.av'
flights = Avia(flights_with_time())


def sorting_top(departure, arrival):
    d = str(departure)
    a = str(arrival)
    lof = flights[d].routes(a, 4)
    b = []
    final_list = []
    for x in lof:
        a = (x, [len(airlines_change(x)), total_time(x), total_cost(x)])
        b.append(a)
    for i in sorted(b, key=lambda e: (e[-1][0], len(e[0]), e[-1][1], e[-1][2])):
        final_list.append(i[0])
    return final_list


def sorting_cheap(departure, arrival):
    d = str(departure)
    a = str(arrival)
    lof = flights[d].routes(a, 4)
    b = []
    final_list = []
    for x in lof:
        a = (x, [total_cost(x), len(airlines_change(x)), total_time(x)])
        b.append(a)
    for i in sorted(b, key=lambda e: (e[-1][0], e[-1][1], len(e[0]), e[-1][2])):
        final_list.append(i[0])
    return final_list


def output(choice):
    if not choice:
        return 'Unfortunately, there are no such flights!'
    for i in range(len(choice[0]) - 1):
        if check_40_mins(choice[0][i].Arrival, choice[0][i+1].Departure):
            return ', '.join('{0.From} {0.Departure} -> {0.To} {0.Arrival} {0.Airlines} ({0.Cost})'.format(f) for f in choice[0])



def output_N(choice, number, N=0):
    if not choice:
        return 'Unfortunately, there are no such flights!'
    for route in choice:
        if N < int(number):
            for i in range(len(route) - 1):
                if check_40_mins(route[i].Arrival, route[i+1].Departure):
                    N += 1
                    print(', '.join('{0.From} {0.Departure} -> {0.To} {0.Arrival} {0.Airlines} ({0.Cost})'.format(f) for f in route))
                    break


def main():
    arg = sys.argv
    try:
        if arg[1] == 'add':
            with open(file, 'a+') as f:
                f.writelines("\n" + 'From: ' + arg[2] + "\n" +
                            'To: ' + arg[3] + "\n" +
                            'Departure: ' + arg[4] + "\n" +
                            'Arrival: ' + arg[5] + "\n" +
                            'Cost: $' + arg[6] + "\n" +
                            'Airlines: ' + arg[7])

        elif arg[1] == 'top':
            if len(arg) > 4:
                return output_N(sorting_top(arg[2], arg[3]), arg[4])
            else:
                print(output(sorting_top(arg[2], arg[3])))

        elif arg[1] == 'find-cheap' :
            if len(arg) > 4:
                return output_N(sorting_cheap(arg[2], arg[3]), arg[4])
            else:
                print(output(sorting_cheap(arg[2], arg[3])))

    except IndexError:
        pass

if __name__ == '__main__':
    main()
