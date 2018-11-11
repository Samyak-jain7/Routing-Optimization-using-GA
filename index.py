import random
from fitness import FitnessFunction,visualize

# Constant Parameters

n = 10      # Mesh size(n x n)
xy =  {}    # Stores coordinate in xy form
val = {}    # Stores value at coordinate

for i in range(1, n+1):
    for j in range(1, n+1):
        xy[n*i-n+j] = (i-1, j-1)
        val[(i-1, j-1)] = n*i-n+j

num_of_chromosome = 10     # number of chromosome
num_of_sourcedest = 10     # number of source-destination pairs
source = [1, 3, 5, 6, 8, 12, 15, 19, 23, 25]
destination = [16, 13, 50, 90, 100, 60, 65, 40, 43, 55]


def generate_path(source, destination):
    path = []
    path.append(source)
    d = destination
    while destination not in path:
        x = xy[path[-1]][0]
        y = xy[path[-1]][1]
        if x < xy[d][0] and y < xy[d][1]:
            path.append(random.choice([val[(x+1, y)], val[(x, y+1)]]))
        elif x > xy[d][0] and y > xy[d][1]:
            path.append(random.choice([val[(x-1, y)], val[(x, y-1)]]))
        elif x > xy[d][0] and y < xy[d][1]:
            path.append(random.choice([val[(x-1, y)], val[(x, y+1)]]))
        elif x < xy[d][0] and y > xy[d][1]:
            path.append(random.choice([val[(x+1, y)], val[(x, y-1)]]))
        elif x == xy[d][0] and y < xy[d][1]:
            path.append(val[(x, y+1)])
        elif x == xy[d][0] and y > xy[d][1]:
            path.append(val[(x, y-1)])
        elif x < xy[d][0] and y == xy[d][1]:
            path.append(val[(x+1, y)])
        elif x > xy[d][0] and y == xy[d][1]:
            path.append(val[(x-1, y)])
    return path


def initialize():
    population = []
    for _ in range(num_of_chromosome):
        chromosome = []
        # making zipped list for source-destination pair
        l = list(zip(source, destination))
        for i in range(num_of_sourcedest):
            chromosome.append(generate_path(*l[i]))
        population.append(chromosome)
    return population


def show(population):
    for chromosome in population:
        print(chromosome)
        print('')


population = initialize()
show(population)
print()
visualize(FitnessFunction(population[0]))
# show(pop)
