# srat-solver

Python 3 implementation of a genetic algorithm for solving Jim Propp's [Self-Referential Aptitude Test](http://faculty.uml.edu/jpropp/srat.html).

## Running

`python srat_solver.py` outputs either the number of generations required to reach the answer (eg. `84`), or a message stating why the algorithm was unsuccessful (eg. `There were no survivors at generation 80.`).

## Testing

`python -m doctest srat_verify.py` will run all existing tests.
