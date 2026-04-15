import random


CHROMOSOME_LENGTH = 8
POPULATION_SIZE = 6
MUTATION_RATE = 0.1
MAX_GENERATIONS = 50

def create_chromosome():
    return [random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]

def create_population():
    return [create_chromosome() for _ in range(POPULATION_SIZE)]

def fitness(chromosome):
    return sum(chromosome)

def select_parent(population):
    fitness_values = [fitness(c) for c in population]
    total_fitness = sum(fitness_values)

    probabilities = [f / total_fitness for f in fitness_values]
    selected_index = random.choices(range(len(population)), weights=probabilities)[0]
    return population[selected_index]

def crossover(parent1, parent2):
    point = random.randint(1, CHROMOSOME_LENGTH - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(chromosome):
    for i in range(len(chromosome)):
        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]
    return chromosome

def main():
    population = create_population()

    for generation in range(MAX_GENERATIONS):
        population = sorted(population, key=fitness, reverse=True)
        best = population[0]

        print(f"Generation {generation}")
        print("Best Chromosome:", best, "Fitness:", fitness(best))
        print("-" * 40)

        if fitness(best) == CHROMOSOME_LENGTH:
            print("\nOptimal solution found!")
            break

        new_population = []

        for _ in range(POPULATION_SIZE // 2):
            parent1 = select_parent(population)
            parent2 = select_parent(population)

            child1, child2 = crossover(parent1, parent2)

            child1 = mutate(child1)
            child2 = mutate(child2)

            new_population.extend([child1, child2])

        population = new_population

    print("\nFinal Solution:", population[0])
