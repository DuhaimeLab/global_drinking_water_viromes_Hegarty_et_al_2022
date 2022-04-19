# global_drinking_water_viromes_Hegarty_et_al_2022

Repository to accompany "A Snapshot of the Global Drinking Water Virome: Diversity and Metabolic Potential Vary with Residual Disinfectant Use", Hegarty, et al 2021.

This code provides the scripts necessary to replicate the analyses described in the paper.

## Identifying Viral Sequences

To identify a set of possible contigs:
- Snakefile-checkv
- Snakefile-vibrant
- Snakefile-virfinder
- Snakefile-virsorter
- Snakefile-virsorter2

Then to build the set of high confidence viral populations:
- identifying_viral_contigs_redoing.Rmd
- Snakefile-getviraltrimmed
- slurm_clusterviruses.sh
- Snakefile-sample2assembly
- Snakefile-sample2assemblyviralreads
- Snakefile-viralseqcoords

## Taxonomy and Functional Annotation

To annotate the ORFs and get taxonomic assignments:
- DRAM_slurm.sh
- slurm_vcontact2.sh

To quantify the coverage to each ORF:
- dram_featureCounts

The following R notebooks were used to analyze the diversity and functional potential of the viral populations:
- drinking_water_metaanalysis_taxa_counts_processing_redoing.Rmd
- drinking_water_metaanalysis_taxa_figure_generation_redoing.Rmd
- drinking_water_metaanalysis_orf_counts_processing_redoing.Rmd
- drinking_water_metaanalysis_orf_deseq_redoing.Rmd
- drinking_water_metaanalysis_orf_Dai_pathway_modules_redoing.Rmd
- drinking_water_metaanalysis_orf_beta_diversity_redoing.Rmd
- taxonomy_redoing.Rmd



