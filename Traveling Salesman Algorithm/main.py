import googlemaps
from itertools import permutations
from tqdm import tqdm

def geocode_address(client, address):
    geocode_result = client.geocode(address)
    lat_lng = geocode_result[0]['geometry']['location']
    return lat_lng

def calculate_distance(client, origins, destinations, cache):
    distances = []
    for origin, destination in zip(origins, destinations):
        if (origin, destination) in cache:
            distance = cache[(origin, destination)]
        else:
            origin_coords = geocode_address(client, origin)
            dest_coords = geocode_address(client, destination)
            distance = client.distance_matrix(origin_coords, dest_coords, mode="driving")["rows"][0]["elements"][0]["distance"]["value"]
            cache[(origin, destination)] = distance
            cache[(destination, origin)] = distance  # Symmetric, so cache both directions
        distances.append(distance)
    return distances

def find_shortest_route(addresses, api_key):
    client = googlemaps.Client(api_key)
    permutations_list = permutations(addresses)
    min_distance = float("inf")
    optimal_route = None
    cache = {}

    pbar = tqdm(permutations_list, desc="Calculating Distances", unit="permutation")
    for permutation in pbar:
        distances = calculate_distance(client, permutation, permutation, cache)
        route_distance = sum(distances[i] for i in range(len(permutation)-1))
        if route_distance < min_distance:
            min_distance = route_distance
            optimal_route = permutation

    return optimal_route

# Example usage
addresses = [
    "1828 S Milpitas Blvd, Milpitas, CA",
    "4424 Camden St, Oakland, CA",
    "11280 64th Ave, Oakland, CA",
    "4175 Bayo St, Oakland, CA",
    "5316 Cole St, Oakland, CA",
    "4722 Congress Ave, Oakland, CA",
    "442 Nabor St, San Leandro, CA",
    "1614 52nd Ave, Oakland, CA",
    "1625 Church St, Oakland, CA",
    "3323 Suter St, Oakland, CA",
]

api_key = "HEHE"  # Replace with your actual API key
optimal_route = find_shortest_route(addresses, api_key)

print("Optimal Route:")
for address in optimal_route:
    print(address)
