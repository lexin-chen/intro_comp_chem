#!/bin/bash
#SBATCH --job-name=water.job
#SBATCH --output=water.out
#SBATCH --error=water.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=le.chen@ufl.edu
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 # number of CPU core to use
#SBATCH --account=chm6586
#SBATCH --qos=chm6586

cd $SLURM_SUBMIT_DIR
module load gaussian
which g09
g09 < ch3cho_freq.com  > ch3cho_freq.log
