#!/bin/bash
#SBATCH --mail-type=ALL
#SBATCH --mail-user=davidvng@usc.edu
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=12
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=2
#SBATCH --mem-per-cpu=2GB
#SBATCH --time=48:00:00
#SBATCH --output=lcdm_lmax800.log

srun python3 lcdm_lmax800.py
