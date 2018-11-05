import random

# Constant Parameters

n = 4
source = [1, 3, 5, 6]
destination = [7, 10, 15, 16]
t_row = []       # top row
b_row = []       # bottom row
l_col = []       # left column
r_col = []       # right column

for i in range(1, n+1):
    t_row.append(i)
for i in range(n*(n-1)+1, n*n+1):
    b_row.append(i)
for i in range(1, n*(n-1)+2, n):
    l_col.append(i)
for i in range(n, n*n+1, n):
    r_col.append(i)


# Generating Population

 # s = source and d = destination
def generate_path(s, d):
    path = []
    k = random.randint(3, 2*n-2)
    path.append(s)
    i = 0
    while i < k-1:
        if path[i] in t_row:
            if path[i] == 1:
                k = random.choice([path[i]+1, path[i]+n])
                if k not in path:
                    path.append(k)
                    i += 1
                # path.append(random.choice([path[i]+1,path[i]+n]))
            elif path[i] == n:
                k = random.choice([path[i]-1, path[i]+n])
                if k not in path:
                    path.append(k)
                    i += 1
                # path.append(random.choice([path[i]-1,path[i]+n]))
            else:
                k = random.choice([path[i]+1, path[i]-1, path[i]+n])
                if k not in path:
                    path.append(k)
                    i += 1
                # path.append(random.choice([path[i]+1,path[i]-1,path[i]+n]))
        elif path[i] in b_row:
            if path[i] == n*(n-1)+1:
                k = random.choice([path[i]+1, path[i]-n])
                if k not in path:
                    path.append(k)
                    i += 1
                # path.append(random.choice([path[i]+1,path[i]-n]))
            elif path[i] == n*n:
                k = random.choice([path[i]-1, path[i]-n])
                if k not in path:
                    path.append(k)
                    i += 1
                # path.append(random.choice([path[i]-1,path[i]-n]))
            else:
                k = random.choice([path[i]+1, path[i]-1, path[i]-n])
                if k not in path:
                    path.append(k)
                    i += 1
                # path.append(random.choice([path[i]+1,path[i]-1,path[i]-n]))
        elif path[i] in l_col:
            k = random.choice([path[i]+n, path[i]-n, path[i]+1])
            if k not in path:
                path.append(k)
                i += 1
            # path.append(random.choice([path[i]+n,path[i]-n,path[i]+1]))
        elif path[i] in r_col:
            k = random.choice([path[i]+n, path[i]-n, path[i]-1])
            if k not in path:
                path.append(k)
                i += 1
            # path.append(random.choice([path[i]+n,path[i]-n,path[i]-1]))
        else:
            k = random.choice([path[i]+1, path[i]-1, path[i]+n, path[i]-n])
            if k not in path:
                path.append(k)
                i += 1
            # path.append(random.choice([path[i]+1,path[i]-1,path[i]+n,path[i]-n]))
        # print(i)
    return path


def initialize():
    population = []
    for _ in range(10):
        chromosome = []
        # making zipped list for source-destination pair
        l = list(zip(source, destination))
        for i in range(4):
            chromosome.append(generate_path(*l[i])
        population.append(chromosome)
    return population


def show(population):
    for chromosome in pop:
        print(chromosome)
        print('')

pop=initialize()
show(pop)
