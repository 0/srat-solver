from simple_genetic import PlagueError, Runner
from srat_verify import works

def fitness(ans):
	c = 0

	for w in works:
		if w(ans.value()):
			c += 1

	return c / len(works)

g = Runner(fitness, 'ABCDE', num_genes=len(works), odds_mating=0.50, odds_mutation=0.15, pop_size=1000, fitness_cutoff=0.50)

try:
	soln, gen = g.run()

	if soln != "DADBEDDEDABADBADBABE":
		raise ValueError("Incorrect solution!")

	print(gen)
except PlagueError as e:
	print(e)
