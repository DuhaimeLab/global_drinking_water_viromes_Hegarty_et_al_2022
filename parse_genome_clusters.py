import sys

print("started")
with open(sys.argv[2], 'wt') as outfile:
    outfile.write("cluster\tcontig\tlength\n")
    with open(sys.argv[1], 'rt') as viralclusterlist:
        for line in viralclusterlist:
            if (">" in line):
                line=line.replace(">", "")
                cluster=line.split('\t')[0]
                outfile.write(line)
            else:
                contig=line.split('\t')[0]
                length=line.split('\t')[2]
                outfile.write("%s\t%s\t%s" % (cluster, contig, length))
print("done")