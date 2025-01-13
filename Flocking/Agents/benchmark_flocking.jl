using Agents
using BenchmarkTools
using Random

include("Flocking.jl")

rng_seed = MersenneTwister(42)

rng_model() = Xoshiro(rand(rng_seed, 1:10000))

#function run_model(rng, extent, n_birds, visual_distance)
#    model = flocking_model(rng, extent, n_birds, visual_distance)
#    step!(model, 100)
#end

n_run = 10

a_small = @benchmark step!(model, 100) setup = (
    rng = rng_model();
    model = flocking_model(rng, (200, 200), 1000, 10.0)
) evals=1 samples=n_run seconds=1e6
median_time = sort(a_small.times)[n_run ÷ 2 + n_run % 2]
println("Agents.jl Flocking-small (ms): ", median_time * 1e-6)


a_large = @benchmark step!(model, 100) setup = (
    rng = rng_model();
    model = flocking_model(rng, (500, 500), 10000, 10.0)
) evals=1 samples=n_run seconds=1e6
median_time = sort(a_large.times)[n_run ÷ 2 + n_run % 2]
println("Agents.jl Flocking-large (ms): ", median_time * 1e-6)

