from simple_genetic import PlagueError, Runner
from srat_verify import works

def fitness(ans):
	"""Normalized fitness for an SRAT individual."""
	c = 0

	# Check the answer for each question.
	for w in works:
		if w(ans.value()):
			# Assume each question has the same relative importance.
			c += 1

	# Fraction of correct answers.
	return c / len(works)

g = Runner(fitness, 'ABCDE', num_genes=len(works), odds_mating=0.50, odds_mutation=0.15, pop_size=1000, fitness_cutoff=0.50)

try:
	soln, gen = g.run()

	# Check against the known solution.
	if soln != "DADBEDDEDABADBADBABE":
		raise ValueError("Incorrect solution!")

	print(gen)
except PlagueError as e:
	print(e)
