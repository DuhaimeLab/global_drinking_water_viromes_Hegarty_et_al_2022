arrayid=$(($1 + 1))

samplename=$(sed -n "${arrayid}p" /scratch/kwigg_root/kwigg/hegartyb/SnakemakeAssemblies3000/CompetitiveMapping/Config/assemblies_list.txt)

mkdir ${samplename}

DRAM.py annotate -i /scratch/kwigg_root/kwigg/hegartyb/SnakemakeAssemblies3000/CompetitiveMapping/ViralSeqsTrimmed/${samplename}_3000_viralonly.fa -o /scratch/kwigg_root/kwigg/hegartyb/SnakemakeAssemblies3000/CompetitiveMapping/DRAM/${samplename}/Annotation --low_mem_mode --threads 10

DRAM.py distill -i /scratch/kwigg_root/kwigg/hegartyb/SnakemakeAssemblies3000/CompetitiveMapping/DRAM/${samplename}/Annotation/annotations.tsv -o /scratch/kwigg_root/kwigg/hegartyb/SnakemakeAssemblies3000/CompetitiveMapping/DRAM/${samplename}/GenomeSummaries --trna_path /scratch/kwigg_root/kwigg/hegartyb/SnakemakeAssemblies3000/CompetitiveMapping/DRAM/${samplename}/Annotation/trnas.tsv --rrna_path /scratch/kwigg_root/kwigg/hegartyb/SnakemakeAssemblies3000/CompetitiveMapping/DRAM/${samplename}/Annotation/rrnas.tsv

