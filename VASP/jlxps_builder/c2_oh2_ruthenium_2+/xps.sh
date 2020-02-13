#!/bin/bash 
mkdir poscarxps
cp ./xps-icorelevel10-static/POSCAR ./poscarxps
cd poscarxps
carbon=25
max=$((carbon - 1)) 
j=$(sed -n '/Direct/=' POSCAR) 
t=$((j + 1))
v=$((t + 1))

for ((i=1; i <= $max; ++i))
do
#cp ./POSCAR POSCAR"$i"

l=$(($t + $i))
echo $t
echo $l
# Switch lines for each POSCAR file

if [ $l != $v ] ;
then
awk -v var="$t" -v var1="$l" 'NR==var {
  s=$0
  for(k=var+1;k<var1;k++){
    getline;s1=s1?s1 "\n" $0:$0
  }
   getline;print;print s1 "\n" s
 next
}1' <POSCAR> POSCAR"$i"

else

awk -v var="$t" -v var1="$l" 'NR==var {
  s=$0
  for(k=var+1;k<var1;i++){
    getline;s=$0"\n"s
  }
  getline;print;print s
  next  
}1' <POSCAR> POSCAR"$i"

fi 
done 
cd ../
for ((p=1; p <= $max; ++p))
do
  cp -r xps-icorelevel10-static xps-icorelevel1"$p"-static
  cd xps-icorelevel1"$p"-static
  rm slurm* vasp* POSCAR
  mv ../poscarxps/POSCAR"$p" ./POSCAR
  mv job.sh job"$p".sh
  sbatch job"$p".sh
  cd ..
done
