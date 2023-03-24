#!/bin/bash
#SBATCH --account=chm6586
#SBATCH --qos=chm6586
#SBATCH --job-name=cpptraj
#SBATCH --output=cpptraj.out
#SBATCH --error=cpptraj.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --distribution=block:block
#SBATCH --time=7-00:00:00
#SBATCH --mem-per-cpu=40gb
#SBATCH --partition=gpu
#SBATCH --gres=gpu:a100:1

#SBATCH --mail-type=all
#SBATCH --mail-user=le.chen@ufl.edu


module load cuda/11.1.0 nvhpc/20.11 openmpi/4.0.5 amber/20
ml vmd
cd $SLURM_SUBMIT_DIR

cpptraj minimage.in

