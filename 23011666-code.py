import random# Import the random module for generating random numbers.

def initialize_population(size):# Function to initialize a population of individuals, each representing a solution.
    return [random.sample(range(8), 8) for _ in range(size)]# Create a list of individuals, each is a random permutation of numbers 0-7

def fitness(individual):# Function to calculate the fitness of an individual.
    non_attacking = 0 # Counter for non-attacking pairs of queens.
    for i in range(len(individual)): # Iterate over each queen in the individual.
        for j in range(i + 1, len(individual)):# Compare with every other queen ahead in the list
            if individual[i] != individual[j] and abs(i - j) != abs(individual[i] - individual[j]):# Check if queens are not attacking each other.
                non_attacking += 1 # Increment counter if queens are not attacking
    return non_attacking # Return the count of non-attacking pairs

def select(population, fitnesses):# Function to select two individuals from the population based on their fitness.
    return random.choices(population, weights=fitnesses, k=2)# Use weighted random selection to pick two individuals.

def crossover(parent1, parent2):# Function to perform crossover between two parents to produce offspring
    point = random.randint(1, 7)# Choose a random point for crossover
    child1 = parent1[:point] + parent2[point:]# Create two children by combining parts of the parents' genomes.
    child2 = parent2[:point] + parent1[point:]
    return child1, child2 # Return the two offspring.

def mutate(individual):# Function to mutate an individual by changing a random element in its genome.
    index = random.randint(0, 7) # Choose a random index for mutation
    value = random.randint(0, 7) # Choose a random value for mutation.
    individual[index] = value # Perform the mutation by changing the genome at the chosen index
    return individual # Return the mutated individual.

def genetic_algorithm():# Main function to run the genetic algorithm.
    population = initialize_population(100)# Initialize a population of 100 individuals.
    generation = 0 # Start counting generations from 0
    while True:# Start an infinite loop to evolve the population
        fitnesses = [fitness(ind) for ind in population]#Calculate fitness for each individual.
        if max(fitnesses) == 28:  # If the maximum fitness is 28 (solution found), break the loop.
            break
        parents = select(population, fitnesses)# Select two parents for reproduction.
        offspring = crossover(*parents)# Create offspring through crossover
        offspring = [mutate(child) for child in offspring]#Mutate the offspring
        population = population[:-2] + offspring # Replace the least fit individuals with offspring
        generation += 1 # Increment the generation count.
    solution = population[fitnesses.index(max(fitnesses))]#Find the individual with the highest fitness.
    return solution, generation # Return the solution and the number of generations

solution, generations = genetic_algorithm() # Execute the genetic algorithm and print the solution and number of generations.
print(f'Solution: {solution} found in {generations} generations') # Output the solution and generation count.
