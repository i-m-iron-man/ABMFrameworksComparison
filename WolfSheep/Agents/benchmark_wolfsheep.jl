using Agents
using BenchmarkTools
using Random

include("WolfSheep.jl")

rng_seed = MersenneTwister(42)

# Function to produce a random RNG for each benchmark run
rng_model() = Xoshiro(rand(rng_seed, 1:10000))

# Create the model *once* in the setup block (untimed),
# then measure only the step! call.
n_run = 10

a_small = @benchmark step!(model, 100) setup = (
    rng = rng_model();
    model = predator_prey_model(rng, 1000, 500, (100, 100), 10, 0.4, 0.2)
) evals=1 samples=n_run seconds=1e6

median_time = sort(a_small.times)[n_run ÷ 2 + n_run % 2]
println("Agents.jl WolfSheep-small (ms): ", median_time * 1e-6)


a_large = @benchmark step!(model, 100) setup = (
    rng = rng_model();
    model = predator_prey_model(rng, 10000, 5000, (1000, 1000), 40, 0.5, 0.2)
) evals=1 samples=n_run seconds=1e6


median_time = sort(a_large.times)[n_run ÷ 2 + n_run % 2]
println("Agents.jl WolfSheep-large (ms): ", median_time * 1e-6)

