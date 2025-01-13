# Agent based modelling frameworks comparison
This repository contains code that we forked and modified from [here](https://github.com/JuliaDynamics/ABMFrameworksComparison.git).
The chief modification present here is that we note just the time of execution of models by these frameworks and omit the model setup and compilation time.
This is done because JAX takes [much more time to compile and setup on a hardware accelerator like GPU compared to Julia](https://kidger.site/thoughts/jax-vs-julia/#:~:text=Julia%20is%20a%20programming%20language,we%20get%20things%20like%20jax.).
To run these frameworks on the benchmark tasks, you can follow the setup instructions in the [original repository](https://github.com/JuliaDynamics/ABMFrameworksComparison.git) and just swap the 
respective directories from this repository.

