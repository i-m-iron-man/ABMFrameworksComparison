# Use Python 3

# Only collect the number of wolves and sheeps per step.

import timeit
import gc

setup = """
gc.enable()
import os, sys
sys.path.insert(0, os.path.abspath("."))

from agents import Sheep, Wolf, GrassPatch
from WolfSheep import WolfSheep

import random
random.seed(42)

seed = random.randint(1, 10000)
height = 1000
width = 1000
initial_sheep = 10000
initial_wolves = 5000
sheep_reproduce = 0.5
wolf_reproduce = 0.2
grass_regrowth_time = 40

wolfsheep = WolfSheep(seed, height, width, initial_sheep, initial_wolves, sheep_reproduce, wolf_reproduce, grass_regrowth_time)

def runthemodel():
    for i in range(0, 100):
      wolfsheep.step()
"""

n_run = 10

tt = timeit.Timer('runthemodel()', setup=setup.format())
a = tt.repeat(n_run, 1)
median_time = sorted(a)[n_run // 2 + n_run % 2]
print("Mesa WolfSheep-large (ms):", median_time*1e3)

setup = """
gc.enable()
import os, sys
sys.path.insert(0, os.path.abspath("."))

from agents import Sheep, Wolf, GrassPatch
from WolfSheep import WolfSheep

import random
random.seed(42)

seed = random.randint(1, 10000)
height = 100
width = 100
initial_sheep = 1000
initial_wolves = 500
sheep_reproduce = 0.4
wolf_reproduce = 0.2
grass_regrowth_time = 20

wolfsheep = WolfSheep(seed, height, width, initial_sheep, initial_wolves, sheep_reproduce, wolf_reproduce, grass_regrowth_time)

def runthemodel():
    for i in range(0, 100):
      wolfsheep.step()
"""

n_run = 10

tt = timeit.Timer('runthemodel()', setup=setup.format())
a = tt.repeat(n_run, 1)
median_time = sorted(a)[n_run // 2 + n_run % 2]
print("Mesa WolfSheep-small (ms):", median_time*1e3)
