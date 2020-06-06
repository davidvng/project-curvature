#!/bin/bash
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=6
#SBATCH --mem-per-cpu=2GB
#SBATCH --time=24:00:00

srun python3 clusterLCDM_test.py
