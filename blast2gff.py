import sys

seqtype=sys.argv[3]

with open(sys.argv[2], 'wt') as outfile:
    outfile.write("##gff-version 3\n")
    with open(sys.argv[1], 'rt') as matches:
        previous=""
        count=1
        start_prev=0
        end_prev=0
        for line in matches:
            seqid=line.split('\t')[1]
            seqid_mod=seqid.replace('.', '_')
            start=int(line.split('\t')[8])
            end=int(line.split('\t')[9])
            viralseq=line.split('\t')[0]
            percentage=line.split('\t')[2]
            length=int(line.split('\t')[3])
            direction=int(start)-int(end)
            #only keep sequences where the viral trimmed contig comes from the contig
            if (seqid_mod in viralseq):
                #make sure it is an exact match
                if (percentage=='100.000'):
                    #don't keep short matches
                    if (length > 1000):
                        #only keep viral contigs mapping in the correct direction (direction < 0)- most were included within the correct direction
                        if (direction<0):
                            strand="+"
                            if (viralseq!=previous):
                                count=1
                                start_prev=0
                                end_prev=0        
                            if (start_prev>end or end_prev<start):
                                outfile.write("%s\tViral_Contigs\t%s\t%s\t%s\t.\t%s\t.\tID=%s||viral_frag_%s\n" % (seqid, seqtype, start, end, strand, viralseq, count))
                            elif (start<end_prev and end>end_prev):
                                start=end_prev+1
                                outfile.write("%s\tViral_Contigs\t%s\t%s\t%s\t.\t%s\t.\tID=%s||viral_frag_%s\n" % (seqid, seqtype, start, end, strand, viralseq, count))
                            elif (start<start_prev and end>start_prev):
                                end=start_prev-1
                                outfile.write("%s\tViral_Contigs\t%s\t%s\t%s\t.\t%s\t.\tID=%s||viral_frag_%s\n" % (seqid, seqtype, start, end, strand, viralseq, count)) 
                            if (viralseq==previous):
                                if (start_prev>start):
                                    start_prev=start
                                if (end_prev<end):
                                    end_prev=end  
                            count+=1 
            previous=viralseq
