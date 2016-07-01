
import csv
import argparse

parser = argparse.ArgumentParser(description='choose heaviest weight from csv')
parser.add_argument('edges', type=argparse.FileType('r'), help="path to weighted edges file" )
args = parser.parse_args()


r = csv.reader(args.edges)

byweight = {}

for e in r:
    (s,t,w) = e
    if (s,t) in byweight:
        if w > byweight[(s,t)]:
            byweight[(s,t)] = w
    else:
        byweight[(s,t)]=w



for e in byweight:
    print ",".join([e[0],e[1],byweight[(s,t)]])
