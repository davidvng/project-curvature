#!/bin/bash
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=6
#SBATCH --mem-per-cpu=2GB
#SBATCH --time=24:00:00
#SBATCH --mail-user=davidvng@usc.edu
#SBATCH --mail-type=ALL
#SBATCH --output=lcdm_log

srun python3 lcdm_highTT+lowEE.py
