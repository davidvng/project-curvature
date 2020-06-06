#!/bin/bash
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=6
#SBATCH --mem-per-cpu=2GB
#SBATCH --time=24:00:00
#SBATCH --mail-user=sarnaaik@usc.edu
#SBATCH --mail-type=ALL


srun python3 flatomegak_test.py
