import Bio
from Bio import SeqIO

with open(snakemake.output["fasta"], 'wt') as outfile:
    with open(snakemake.input["clist"], 'rt') as viralcontigslist:
        contigs = []
        i = 0
        j = 0
        for line in viralcontigslist:
            if (i==0):
                i += 1
            else:
                i+=1
                assembly=line.split('\t')[int(snakemake.params["asssembly_column"])].strip("\n")
                #if (i==2):
                #print("assembly:%s" % assembly)
                #print("params:%s" % snakemake.params["assembly"])
                if (assembly==snakemake.params["assembly"]):
                    contig = line.split('\t')[int(snakemake.params["contig_column"])]
                    contigs.append(contig)
                    j+=1
                    #print("here")
        print(i)
        print("contigs count: %s" % j)

        i = 0

        #virsorter2
        filename = snakemake.input["virsorter2_fasta"]
        for seqrecord in SeqIO.parse(filename,"fasta"):
            comp = seqrecord.id
            comp2 = comp.replace(".", "_")
            comp = comp2.split("|")[0]
            if (comp in contigs):
                i+=1
                contigs.remove(comp)
                outfile.write(">%s--%s\n%s\n" % (snakemake.params["assembly"], comp2, seqrecord.seq))
        print("matches after virsorter2count: %s" % i)

        #checkV
        filename = snakemake.input["checkv_fasta"]
        for seqrecord in SeqIO.parse(filename,"fasta"):
            comp = seqrecord.id
            comp2 = comp.replace(".", "_")
            comp = comp2.split(" ")[0].rsplit("_",1)[0]
            if (comp in contigs):
                i+=1
                contigs.remove(comp)
                outfile.write(">%s--%s\n%s\n" % (snakemake.params["assembly"], comp2, seqrecord.seq))
        print("matches from checkv count: %s" % i)

        #vibrant
        filename = snakemake.input["vibrant_fasta"]
        for seqrecord in SeqIO.parse(filename,"fasta"):
            comp = seqrecord.id
            comp = comp.replace(".", "_")
            if (comp in contigs):
                i+=1
                contigs.remove(comp)
                outfile.write(">%s--%s\n%s\n" % (snakemake.params["assembly"], comp, seqrecord.seq))
        print("matches after vibrant count: %s" % i)

        #free viruses
        filename = snakemake.input["free_fasta"]
        for seqrecord in SeqIO.parse(filename,"fasta"):
            comp = seqrecord.id
            comp = comp.replace(".", "_")
            if (comp in contigs):
                i+=1
                contigs.remove(comp)
                outfile.write(">%s--%s\n%s\n" % (snakemake.params["assembly"], comp, seqrecord.seq))

        print("matches count: %s" % i)

print("done")