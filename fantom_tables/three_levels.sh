
# create three levels from interaction_weights.csv, starting from MEF2C onwards


# L1
awk -F ',' '{if ($1=="MEF2C" && $6>=2) print $1","$4","$6}' interaction_weights.csv > l1_repeats.csv
python ../heavier_weight.py l1_repeats.csv > l1.csv


# L2
awk -F ',' '{print $2}' l1.csv > l2_sources.csv
for F in `cat l2_sources.csv`; do echo grep -w \"^$F\" interaction_weights.csv ; done | sh |  awk -F ',' '{if ($6>=2) print $1","$4","$6}' > l2_repeats.csv
 python ../heavier_weight.py l2_repeats.csv > l2.csv


# L3
awk -F ',' '{print $2}' l2.csv > l3_sources.csv
for F in `cat l3_sources.csv`; do echo grep -w \"^$F\" interaction_weights.csv ; done | sh |  awk -F ',' '{if ($6>=2) print $1","$4","$6}' > l3_repeats.csv
python ../heavier_weight.py l3_repeats.csv > l3.csv
