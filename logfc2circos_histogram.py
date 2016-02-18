import csv

from pprint import pprint

chroms = [str(c) for c in range(1,24)] + ['X','Y']


# red gene loci
loci = {}
csvr = csv.reader( open('data/genes_loci.tsv'),  delimiter='\t')
csvr.next()
for row in csvr:
    (chrom, start, end, symbol) = row

    if chrom in chroms:
        loci[symbol] = (chrom,start,end)




# read log fold changes
csvr = csv.reader( open('data/statistics_2wCBat_cy.csv'),  delimiter=',', quotechar='"')
csvr.next()
for row in csvr:
    symbol = row[0]
    if row[0] in loci:
        print "hs"+loci[symbol][0], loci[symbol][1], loci[symbol][2], row[1]
