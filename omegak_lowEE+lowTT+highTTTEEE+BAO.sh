#!/bin/bash
#SBATCH --mail-type=ALL
#SBATCH --mail-user=sarnaaik@usc.edu
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=24
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=2GB
#SBATCH --time=48:00:00
#SBATCH --output=omegak_lowEE+lowTT+highTTTEEE+BAO.log

srun python3 omegak_lowEE+lowTT+highTTTEEE+BAO.py
