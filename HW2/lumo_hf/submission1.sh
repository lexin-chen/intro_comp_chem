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
module load gaussian
which g09
cd $SLURM_SUBMIT_DIR
input=4.com
output=4.log
g09 < $input > $output
