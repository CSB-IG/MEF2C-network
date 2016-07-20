import csv



chroms = [str(c) for c in range(1,24)] + ['X','Y']
# red gene loci
loci = {}
csvr = csv.reader( open('../data/genes_loci.tsv'),  delimiter='\t')
csvr.next()
for row in csvr:
    (chrom, start, end, symbol) = row

    if chrom in chroms:
        loci[symbol] = ("hs%s" % chrom, start, end)



for level in [1,2,3]:
    with open("../fantom_tables/l%s.csv" % level) as l1, \
         open("data/l%s_links.tsv" % level, 'w') as links:
        csvr = csv.reader(l1)
        csvw = csv.writer(links, delimiter=" ")
        for interaction in csvr:
            (s,t,w) = interaction
            if s in loci and t in loci:
                csvw.writerow( loci[s] + loci[t])
