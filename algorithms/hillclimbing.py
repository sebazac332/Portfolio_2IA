import numpy as np
import random

np.random.seed(42)
random.seed(42)

num_cities = 10
cities = np.random.rand(num_cities, 2)

def calculate_distance(route):
    route_extended = np.append(route, [route[0]], axis=0)
    return np.sum(np.sqrt(np.sum(np.diff(route_extended, axis=0)**2, axis=1)))

def create_initial_route(cities):
    return np.array(random.sample(list(cities), len(cities)))

def get_neighbors(route):
    neighbors = []
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            neighbor = route.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def hill_climbing(cities):
    current_route = create_initial_route(cities)
    current_distance = calculate_distance(current_route)

    while True:
        neighbors = get_neighbors(current_route)
        next_route = min(neighbors, key=calculate_distance)
        next_distance = calculate_distance(next_route)
        
        if next_distance >= current_distance:
            break
        
        current_route, current_distance = next_route, next_distance

    return current_route, current_distance

hc_route, hc_distance = hill_climbing(cities)

print("Hill Climbing:")
print("Route:", hc_route)
print("Distance:", hc_distance)