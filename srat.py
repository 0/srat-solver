import simple_genetic
from srat_verify import works

def fitness(ans):
	c = 0.0

	for w in works:
		if w(ans.value()):
			c += 1
	
	return c / 20

g = simple_genetic.Runner(fitness, 'ABCDE', 20, 0.50, 0.15, 1000, 0.50)

try:
	soln, gen = g.run()

	if soln != "DADBEDDEDABADBADBABE":
		raise ValueError("Incorrect solution!")

	print(gen)
except simple_genetic.PlagueError as e:
	print(e)

