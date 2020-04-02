"""  
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, 
and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. 
If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] 
and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', 
you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] 
is also a valid itinerary. However, the first one is lexicographically smaller. 
"""

from collections import deque


def getShortestItinerary(start, itinerary):
    # create adjacency list
    totalFlights = len(itinerary) + 1
    adjList = {}
    for flights in itinerary:
        f = flights[0]
        t = flights[1]
        if f not in adjList:
            adjList[f] = []
        adjList[f].append(t)
    return helper([start], adjList, totalFlights)


def helper(flights, adjList, totalFlights):
    curLocation = flights[-1]
    if len(flights) == totalFlights:
        return flights
    if curLocation not in adjList or not adjList[curLocation]:
        return None

    fullPath = None
    adjList[curLocation].sort()
    for i in range(len(adjList[curLocation])):
        dest = adjList[curLocation][i]
        if dest == '@':
            continue
        adjList[curLocation][i] = '@'
        flightsCopy = flights.copy()
        flightsCopy.append(dest)

        possibleItinerary = helper(flightsCopy, adjList, totalFlights)
        if possibleItinerary and not fullPath:
            fullPath = possibleItinerary
            break
        adjList[curLocation][i] = dest
    return fullPath


itinerary1 = [('A', 'C'), ('A', 'B'), ('B', 'C'), ('C', 'A')]
itinerary2 = [('SFO', 'COM'), ('COM', 'YYZ')]
itinerary3 = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
assert getShortestItinerary('A', itinerary1) == ['A', 'B', 'C', 'A', 'C']
assert getShortestItinerary('COM', itinerary2) == None
assert getShortestItinerary('YUL',
                            itinerary3) == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
