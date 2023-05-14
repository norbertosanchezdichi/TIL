import googlemaps
from itertools import permutations
from multiprocessing import cpu_count
from tqdm.contrib.concurrent import process_map

def geocode_address(client, address, cache):
    if address not in cache:
        geocode_result = client.geocode(address)
        lat_lng = geocode_result[0]['geometry']['location']
        cache[address] = (lat_lng['lat'], lat_lng['lng'])
    return cache[address]

def calculate_partial_distance(client, origins, destinations, cache, min_distance):
    total_distance = 0
    for origin, destination in zip(origins, destinations):
        if (origin, destination) in cache:
            distance = cache[(origin, destination)]
        else:
            origin_coords = origin
            dest_coords = destination
            distance = client.distance_matrix(origin_coords, dest_coords, mode="driving")["rows"][0]["elements"][0]["distance"]["value"]
            cache[(origin, destination)] = distance
            cache[(destination, origin)] = distance  # Symmetric, so cache both directions
        total_distance += distance
        if total_distance > min_distance:
            return float('inf')
    return total_distance

def find_shortest_route_for_permutation(args):
    permutation, client, min_distance, cache = args
    origins = [geocode_address(client, address, cache) for address in permutation]
    destinations = origins[1:] + [origins[0]]
    distance = calculate_partial_distance(client, origins, destinations, cache, min_distance)
    return distance, permutation

def find_shortest_route(addresses, api_key):
    client = googlemaps.Client(api_key)
    permutations_list = list(permutations(addresses))
    min_distance = float("inf")
    optimal_route = None
    cache = {}

    results = process_map(find_shortest_route_for_permutation, [(permutation, client, min_distance, cache) for permutation in permutations_list], max_workers=cpu_count())
    for distance, permutation in results:
        if distance < min_distance:
            min_distance = distance
            optimal_route = permutation

    return optimal_route

# Put the main execution code inside this block
if __name__ == '__main__':
    addresses = [
        "4424 Camden St, Oakland, CA",
        "11280 64th Ave, Oakland, CA",
        "4175 Bayo St, Oakland, CA",
        "5316 Cole St, Oakland, CA",
        "4722 Congress Ave, Oakland, CA"
    ]

    api_key = "AIzaSyDpryff0Fa7UvvyfnF8RcNPX2BJ4O6Am4E"  # Replace with your actual API key
    optimal_route = find_shortest_route(addresses, api_key)

    if optimal_route is None:
        print("Unable to find an optimal route.")
    else:
        print("Optimal Route:")
        for address in optimal_route:
            print(address)
