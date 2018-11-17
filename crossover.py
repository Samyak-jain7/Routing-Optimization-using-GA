import index
import random
import fitness
n = index.num_of_chromosome


def tournament(population):
    # First Tournament
    k = random.randint(2, n)
    l = random.sample(population, k)
    Max = 0
    for chromosome in l:
        if sum(fitness.FitnessValue(chromosome)) > Max:
            chrom1 = chromosome
    
    # Second Tournament
    k = random.randint(2, n)
    l = random.sample(population, k)
    Max = 0
    for chromosome in l:
        if sum(fitness.FitnessValue(chromosome)) > Max:
            chrom2 = chromosome
    
    print(chrom1,chrom2)
