#!/bin/bash
#SBATCH --mail-type=ALL
#SBATCH --mail-user=davidvng@usc.edu
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=12
#SBATCH --nodes=2
#SBATCH --mem-per-cpu=2GB
#SBATCH --time=48:00:00
#SBATCH --output=lcdm_highTT+lowEE_run2.log

srun cobaya-run chains/lcdm_highTT+lowEE
