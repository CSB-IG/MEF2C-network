import csv
from pprint import pprint


features = {}
with open('feature.entrez_gene.tbl.txt') as feattable:
    fr = csv.reader(feattable, delimiter="\t")
    for f in fr:
        (fid,symbol,algo) = f
        features[fid] = symbol



p2p = {}
with open('edge.L2_to_L3_april08.tbl.txt') as f:
    er = csv.reader(f, delimiter="\t")
    for e in er:
        (p1, p2) = e
        p2p[p1] = p2
        p2p[p2] = p1


        
pnames={}
with open('feature.CAGE_L1_promoter.tbl.txt') as f:
    fr = csv.reader(f, delimiter="\t")
    for e in fr:
        (pid, pname) = e
        pnames[pid] = pname

with open('feature.CAGE_L2_promoter.tbl.txt') as f:
    fr = csv.reader(f, delimiter="\t")
    for e in fr:
        (pid, pname) = e
        pnames[pid] = pname

with open('feature.CAGE_L3_promoter.tbl.txt') as f:
    fr = csv.reader(f, delimiter="\t")
    for e in fr:
        (pid, pname) = e
        pnames[pid] = pname
        


        
feat_by_promoter = {}
with open('edge.L3_promoter_Entrez_08May16_EvN.tbl.txt') as promoteredge:
    pr = csv.reader(promoteredge, delimiter="\t")
    for e in pr:
        (pid, fid) = e
        feat_by_promoter[pid] = features[fid]



with open('edge2hop.Entrez_TFmatrix_L2_may08.tbl.txt') as e2h:
    er = csv.reader(e2h, delimiter="\t")
    for e in er:
        (fid, pid, w1, w2) = e

        if p2p[pid] in feat_by_promoter:
            print ",".join((features.get(fid,''),
                           pnames[pid],
                           pnames[p2p[pid]],
                           feat_by_promoter.get(p2p[pid]), 
                           w1, w2))
