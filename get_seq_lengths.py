#!/usr/bin/python

#usage: python get_seq_lengths.py [FASTA] [OUTFILE]
#INNAME: file that want to remove short sequences from
#CUTOFF: size threshold to keep sequences

import Bio
from Bio import SeqIO
import sys

with open(sys.argv[2],'wt') as outfile:
    outfile.write("contig\tlength\n")
    for seq_record in SeqIO.parse(sys.argv[1], "fasta"):
        outfile.write("%s\n%s\n" % (seq_record.id, len(seq_record)))
