#to run: python merge_vs2.py <list of files to combine> <name of merged file>

import sys

with open(sys.argv[2], 'wt') as outfile:
    with open(sys.argv[1]) as assemblylist:
        j=1
        i=1
        for assembly in assemblylist:
            assemblyfile=assembly.strip("\n")
            print(assemblyfile)
            with open(assemblyfile, 'rt') as clusterfile:
            	print("here")
                for line in clusterfile:
                    if (i==1 & j==1):
                        outfile.write(line)
                        j+=1
                        i+=1
                    elif (i>1):
                    	#print(i)
                    	#print(int(sys.argv[2]))
                        outfile.write(line)
                        i+=1
                    else:
                    	i+=1
            i=1