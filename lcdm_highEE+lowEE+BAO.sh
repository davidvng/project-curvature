#!/bin/bash
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=12
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=2
#SBATCH --mem-per-cpu=2GB
#SBATCH --time=48:00:00
#SBATCH --mail-user=sarnaaik@usc.edu
#SBATCH --mail-type=ALL
#SBATCH --output=lcdm_highEE+lowEE+BAO.log

srun python3 lcdm_highEE+lowEE+BAO.py
