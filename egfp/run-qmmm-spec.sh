#!/bin/bash
#SBATCH -J egfp-em
#SBATCH --time=00:20:00
#SBATCH --partition=test

#SBATCH --nodes=1
#SBATCH --tasks-per-node=32
#SBATCH --cpus-per-task=4

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export OMP_PLACES=cores

srun gmx mdrun -s egfp-qmmm-spec.tpr -deffnm egfp-qmmm-spec
