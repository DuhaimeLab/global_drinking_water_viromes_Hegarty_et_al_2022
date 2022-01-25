#!/bin/bash

###############################
#                             #
#  1) Job Submission Options  #
#                             #
###############################

# Name
#SBATCH --job-name=featureCounts

# Resources
# For MPI, increase ntasks-per-node
# For multithreading, increase cpus-per-task
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1gb
#SBATCH --time=08-00:00:00

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

#need to rerun this if update DRAM output
#sed -i -e 's/merged_trimmed_viruses_only_95-85_greater_3000_//g' ../DRAM/genes.annotated.gff

module load singularity

cd /scratch/kwigg_root/kwigg/hegartyb/SnakemakeAssemblies3000/CompetitiveMapping

singularity exec /nfs/turbo/lsa-dudelabs/containers/subreads/subreads.sif featureCounts -p -t CDS -g ID -a ./DRAM/genes.annotated.gff -o ./Feat\
ureCounts/genes.annotated.counted.txt ./Bowtie2/Results/AllContigsRecombinedMapping/Mapped_Reads_align_on_all_recombined_*.bam
