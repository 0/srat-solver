import random as r

"""A simple framework for running a genetic algorithm."""

class PlagueError(Exception):
	"""The entire population is gone!"""
	pass

class Individual():
	"""An individual possessing a single chromosome."""
	def __init__(self, chromosome):
		self.chromosome = chromosome

	def __str__(self):
		return self.value()

	def value(self):
		return ''.join(self.chromosome)

	def mutate(self, v):
		"""Set a random gene to the given value."""
		gene = r.randrange(len(self.chromosome))
		self.chromosome[gene] = v

	def mate(self, other):
		"""Produce a new Individual by combining genes from this Individual and the given one."""
		chromosome = [a if r.random() < 0.5 else b
			for a, b in zip(self.chromosome, other.chromosome)]
		return Individual(chromosome)

class Runner():
	"""A simple genetic solver."""
	def __init__(self, fitness, alleles, num_genes, odds_mating,
			odds_mutation, pop_size, fitness_cutoff, fitness_inc=0.1,
			req_fitness=1.0):
		"""Parameters:
			fitness: Function that evaluates the normalized fitness of an individual.
			alleles: List of possible values a gene can have.
			num_genes: Number of genes in an individual.
			odds_mating: Probability of any individual choosing to mate with another in a single generation.
			odds_mutation: Probability of any individual mutating in a single generation.
			pop_size: Starting and maximum number of individuals.
			fitness_cutoff: Individuals not reaching this fraction of maximum fitness are removed first in case of overpopulation.
			fitness_inc: If cutoff is not sufficient to solve overpopulation, increase necessary minimum fitness by this amount.
			req_fitness: Terminate when an individual with at least this fitness exists.
		"""
		opts = locals().copy()
		del opts['self']

		for opt in opts:
			exec('self.%s = %s' % (opt, opt))

	def new_value(self):
		"""Random valid allele."""
		return r.choice(self.alleles)

	def run(self):
		"""Run the population through multiple generations.
		
		Terminates when there is an individual of the required fitness or no individuals remain."""
		# Initial population has entirely random alleles.
		population = [Individual([self.new_value() for y in range(self.num_genes)])
			for x in range(self.pop_size)]

		generation = 1
		while True:
			# Mutate.
			for individual in population:
				if r.random() < self.odds_mutation:
					individual.mutate(self.new_value())

			# Determine fitness levels.
			max_fitness = max([self.fitness(x) for x in population])
			min_fitness = max_fitness * self.fitness_cutoff

			if max_fitness >= self.req_fitness:
				break

			# Mate.
			offspring = [individual.mate(r.choice(population)) for individual in population
				if r.random() < self.odds_mating]
			population.extend(offspring)

			# Fix overpopulation.
			while len(population) > self.pop_size:
				survivors = [individual for individual in population
					if self.fitness(individual) >= min_fitness]

				if len(survivors) == 0:
					raise PlagueError("There were no survivors at generation %d." % generation)
				else:
					population = survivors
					min_fitness += self.fitness_inc

			generation += 1

		# Value of the most fit individual and its generation.
		return sorted(population, key=self.fitness)[-1].value(), generation
