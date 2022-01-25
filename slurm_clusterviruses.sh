#!/bin/bash
# need to load clustergenomes conda environment

###############################
#                             #
#  1) Job Submission Options  #
#                             #
###############################

# Name
#SBATCH --job-name=clustergenomes

# Resources
# For MPI, increase ntasks-per-node
# For multithreading, increase cpus-per-task
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=70g
#SBATCH --time=20:00:00

# Account
#SBATCH --account=kwigg1
#SBATCH --partition=standard

# Logs
#SBATCH --mail-user=hegartyb@umich.edu
#SBATCH --mail-type=BEGIN,END,FAIL

# Environment
##SBATCH --export=ALL

source /etc/profile.d/http_proxy.sh

#  Show list of CPUs you ran on
echo $SLURM_JOB_NODELIST

cd /nfs/turbo/cee-kwigg/hegartyb/SnakemakeAssemblies3000/Scripts/bin 

export PATH=$PATH:"$PWD"

Cluster_genomes.py -f /scratch/kwigg_root/kwigg/hegartyb/SnakemakeAssemblies3000/CompetitiveMapping/ViralSeqsTrimmed/merged_3000_trimmed_viruses_only_20211112.fa -c 85 -i 95 -o /scratch/kwigg_root/kwigg/hegartyb/SnakemakeAssemblies3000/CompetitiveMapping/ClusterGenomes