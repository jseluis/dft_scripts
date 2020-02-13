#!/bin/bash

NTOT=24
NMIN=320.0
NMAX=330.0
FH=0.6

echo $NTOT $NMIN $NMAX $FH >>energies.out

for i in `seq 0 $NTOT`; do

cd xps-icorelevel1$i-static

rm WAVECAR CHG CHGCAR

XD=$(grep ' 1-  1s   -' OUTCAR | cut -c 14-21)
echo $XD " 1.0" >>../energies.out
cd ..

done;
#gfortran jlxpsbuilder.f -o jlxps
./jlxps < energies.out > spectraxps.out
