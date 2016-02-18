import csv



chroms = [str(c) for c in range(1,24)] + ['X','Y']
# red gene loci
loci = {}
csvr = csv.reader( open('data/genes_loci.tsv'),  delimiter='\t')
csvr.next()
for row in csvr:
    (chrom, start, end, symbol) = row

    if chrom in chroms:
        loci[symbol] = (chrom,start,end)



csvr = csv.reader(open("data/l1.csv"))

for interaction in csvr:
    (s,t) = interaction
    if s in loci and t in loci:
        print "hs"+" ".join(loci[s]),"hs"+" ".join(loci[t])
