import random as r

class PlagueError(Exception): pass

class Individual():
	def __init__(self, chromosome):
		self.chromosome = chromosome

	def __str__(self):
		return self.value()

	def value(self):
		return ''.join(self.chromosome)

	def mutate(self, v):
		self.chromosome[r.choice(xrange(len(self.chromosome)))] = v

	def mate(self, other):
		chromosome = [a if r.random() < 0.5 else b
			for a, b in zip(self.chromosome, other.chromosome)]
		return Individual(chromosome)

class Runner():
	def __init__(self, fitness, alleles, num_genes, odds_mating,
			odds_mutation, pop_size, fitness_cutoff, fitness_inc=0.1,
			req_fitness=1.0):
		opts = locals().copy()
		del opts['self']

		for opt in opts:
			exec('self.%s = %s' % (opt, opt))

	def new_value(self):
		return r.choice(self.alleles)

	def run(self):
		population = [Individual([self.new_value() for y in xrange(self.num_genes)])
			for x in xrange(self.pop_size)]

		generation = 1
		while True:
			for individual in population:
				if r.random() < self.odds_mutation:
					individual.mutate(self.new_value())

			max_fitness = max(map(self.fitness, population))
			min_fitness = max_fitness * self.fitness_cutoff

			if max_fitness >= self.req_fitness:
				break

			offspring = [individual.mate(r.choice(population)) for individual in population
				if r.random() < self.odds_mating]
			population.extend(offspring)

			while len(population) > self.pop_size:
				survivors = [individual for individual in population
					if self.fitness(individual) >= min_fitness]

				if len(survivors) == 0:
					raise PlagueError, "There were no survivors at generation %d." % generation
				else:
					population = survivors
					min_fitness += self.fitness_inc

			generation += 1

		return sorted(population, key=self.fitness)[-1].value(), generation

