import random

# Constant Parameters

n = 4
source = [1, 3, 5]
row = []      
col = []   

for i in range(n*(n-1)+1, n*n+1):
    row.append(i)
for i in range(n,n*n+1,n):
    col.append(i)


# Generating Population

def generate_path():
    path = []
    k = random.randint(3, 2*n-2)
    path.append(random.choice(source))
    for i in range(k-1):
        if path[i] in col:
            path.append(path[i]+n)
        elif path[i] in row:
            path.append(path[i]+1)
        else:
            path.append(random.choice([path[i]+1,path[i]+n]))
    return path

def initialize():
    population = []
    for _ in range(10):
        chromosome = []
        for _ in range(4):
            chromosome.append(generate_path())
        population.append(chromosome)
    return population

def show(population):
    for chromosome in pop:
        print(chromosome)
        print('')

pop = initialize()
show(pop)
