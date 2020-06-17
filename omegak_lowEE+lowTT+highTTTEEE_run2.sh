#!/bin/bash
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=12
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=2
#SBATCH --mem-per-cpu=2GB
#SBATCH --time=48:00:00
#SBATCH --mail-user=sarnaaik@usc.edu
#SBATCH --mail-type=ALL
#SBATCH --output=omegak_lowEE+lowTT+highTTTEEE_run2.log

srun cobaya-run chains/omegak_lowEE+lowTT+highTTTEEE
