with open(snakemake.output["coverage"], 'wt') as outfile:
    v_files = str(snakemake.input["tsv"])
    v_list = v_files.split(" ")
    print("starting")
    for v_new in v_list:
        with open(v_new,'rt') as v:
            name=v_new.split("coverage_")[1].split(".tsv")[0]
            print(name)
            #i=0
            for line in v:
                outfile.write('%s\t%s' %(name, line))
                #i+=1
    print("done")