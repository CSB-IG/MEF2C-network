echo "first degree"
for n in {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,X,Y}; do awk '{print $4}' l1_links.tsv | sort | grep -c hs$n; done
echo "second degree"
for n in {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,X,Y}; do awk '{print $4}' l2_links.tsv | sort | grep -c hs$n; done
echo "third degree"
for n in {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,X,Y}; do awk '{print $4}' l3_links.tsv | sort | grep -c hs$n; done
