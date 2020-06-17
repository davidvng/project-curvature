#!/bin/bash
#SBATCH --ntasks=6
#SBATCH --cpus-per-task=8
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=3
#SBATCH --mem-per-cpu=2GB
#SBATCH --time=48:00:00
#SBATCH --mail-user=sarnaaik@usc.edu
#SBATCH --mail-type=ALL
#SBATCH --output=lcdm_highTTTEEE+lowEE.log

srun python3 lcdm_highTTTEEE+lowEE.py
