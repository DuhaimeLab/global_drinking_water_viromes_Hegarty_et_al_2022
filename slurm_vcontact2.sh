#!/bin/bash

###############################
#                             #
#  1) Job Submission Options  #
#                             #
###############################

# Name
#SBATCH --job-name=vcontact

# Resources
# For MPI, increase ntasks-per-node
# For multithreading, increase cpus-per-task
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=50gb
#SBATCH --time=48:00:00

# Account
#SBATCH --account=kwigg1
#SBATCH --partition=standard

# Logs
#SBATCH --mail-user=hegartyb@umich.edu
#SBATCH --mail-type=BEGIN,END,FAIL

# Environment
##SBATCH --export=ALL

#  Show list of CPUs you ran on, if you're running under PBS
echo $SLURM_JOB_NODELIST

#  Change to the directory you submitted from
if [ -n "$SLURM_SUBMIT_DIR" ]; then cd $SLURM_SUBMIT_DIR; fi
pwd


module load singularity

cd /nfs/turbo/cee-kwigg/hegartyb/SnakemakeAssemblies3000/vContact2

singularity exec /nfs/turbo/lsa-dudelabs/containers/vcontact2/vcontact2.sif vcontact2 --raw-proteins /nfs/turbo/cee-kwigg/hegartyb/SnakemakeAssemblies3000/DRAM/Annotation/genes.faa --rel-mode 'Diamond' --proteins-fp all_gene_to_genome.tsv --db 'ProkaryoticViralRefSeq94-Merged' --pcs-mode MCL --vcs-mode ClusterONE --c1-bin /nfs/turbo/cee-kwigg/hegartyb/SnakemakeAssemblies3000/vContact2/cluster_one-1.0.jar --output-dir vConTACT2_Results_final