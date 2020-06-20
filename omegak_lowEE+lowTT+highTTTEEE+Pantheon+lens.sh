#!/bin/bash
#SBATCH --mail-type=ALL
#SBATCH --mail-user=davidvng@usc.edu
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=24
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=1GB
#SBATCH --time=48:00:00
#SBATCH --output=omegak_lowEE+lowTT+highTTTEEE+Pantheon+lens.log

srun python3 omegak_lowEE+lowTT+highTTTEEE+Pantheon+lens.py
