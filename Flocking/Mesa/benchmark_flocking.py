import timeit
import gc

setup_small = """
gc.enable()
import os, sys
sys.path.insert(0, os.path.abspath("."))

from Flocking import BoidFlockers

import random
random.seed(42)
seed = random.randint(1, 10000)
population = 1000
width = 200
height = 200
vision = 10.0
flock_small = BoidFlockers(seed, population, width, height, vision)

def runthemodel_small():
  for i in range(0, 100):
      flock_small.step()

"""

n_run = 100
tt = timeit.Timer('runthemodel_small()', setup=setup_small.format())
a = tt.repeat(n_run, 1)
median_time = sorted(a)[n_run // 2 + n_run % 2]
print("Mesa Flocking-small (ms):", median_time*1e3)


setup_large = """
gc.enable()
import os, sys
sys.path.insert(0, os.path.abspath("."))

from Flocking import BoidFlockers

import random
random.seed(42)
seed = random.randint(1, 10000)
population = 10000
width = 500
height = 500
vision = 10.0
flock_large = BoidFlockers(seed, population, width, height, vision)

def runthemodel_large():
  for i in range(0, 100):
      flock_large.step()

"""
n_run = 100
tt = timeit.Timer('runthemodel_large()', setup=setup_large.format())
a = tt.repeat(n_run, 1)
median_time = sorted(a)[n_run // 2 + n_run % 2]
print("Mesa Flocking-large (ms):", median_time*1e3)
