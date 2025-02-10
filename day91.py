'''Sridhar wrote down his travel itinerary like as follows:
If he wanted to visit Madrid, Paris, Munich, Warsaw and Kiev in this order, he would write it down like as:
Madrid Paris 100
Paris Munich 200
Munich Warsaw 150
Warsaw Kiev 120

More formally, if he wanted to go from A to B directly and the price is C dollars, then he would write
A B C
on a card. Each move was written on a different card. Sridhar was a great planner, so he would never visit the same place twice. Just before starting his journey, the cards got shuffled. Help Sridhar figure out the actual order of the cards and the total cost of his journey.

Input Format
The first line of the input contains an integer T, the number of test cases. T test cases follow. 
Each case contains an integer N, the number of cities Sridhar is planning to visit. N-1 lines follow. Each line is of the form
Ai Bi Ci
where the i-th line refers to the i-th card after getting shuffled.

Output Format
For each case the output contains N lines, the first N-1 lines should contain the N-1 cards in their proper original order, the N-th line should contain the total cost of the travel.'''
t = int(input())  # Number of test cases
for _ in range(t):
    n = int(input())  # Number of cities
    travel = {}  # Dictionary to store routes
    incoming_count = {}  # To determine the starting city
    total_cost = 0
    
    # Read input and store data
    for _ in range(n - 1):
        A, B, C = input().split()
        C = int(C)
        travel[A] = (B, C)  # Mapping: Start City -> (Destination, Cost)
        incoming_count[B] = incoming_count.get(B, 0) + 1
        if A not in incoming_count:
            incoming_count[A] = 0
        total_cost += C  # Keep track of total cost

    # Find the starting city (it has no incoming route)
    start_city = None
    for city in incoming_count:
        if incoming_count[city] == 0:
            start_city = city
            break

    # Reconstruct and print the journey
    current_city = start_city
    while current_city in travel:
        next_city, cost = travel[current_city]
        print(current_city, next_city, cost)
        current_city = next_city
    
    print(total_cost)  # Print the total cost of the journey
