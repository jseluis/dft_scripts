#!/bin/bash
carbon=25
#nclusters=50

max=$((carbon - 1))

#for ((i=1; i <= $nclusters; ++i)); do
#cd cluster$i-xps

for ((p=0; p <= $max; ++p))
do
cd xps-icorelevel1"$p"-static
#sbatch job*
rm WAVE* slurm* CHG*
cd ..

done

#cd ..
#done
