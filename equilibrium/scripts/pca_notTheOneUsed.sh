#!/bin/bash

directory=$( pwd )

first=false

#no_chol chol


if [ "$first" = true ]
then

#concatenate and fit trajectories
echo miau
for sistema in chol no_chol ; do cd ~/Datos/Max_Planck/AQP0/two-tet-longer/$sistema  ; echo Protein |  gmx trjcat -f */tmp.xtc -o cat.xtc -n 1/aux.ndx -cat -tu ns -b 250 ; echo  Protein tetra1_BB Protein  | gmx trjconv -s 1/production.tpr -f cat.xtc -o tmp1.xtc -center -ur compact -pbc cluster -n 1/aux.ndx ; echo tetra1_BB Protein  | gmx trjconv -s 1/production.tpr -f tmp1.xtc -o tmp2.xtc -center -ur compact -pbc mol -n 1/aux.ndx  >& out || { cat out; exit 1; } ; echo tetra1_BB Protein  | gmx trjconv -f tmp2.xtc -s 1/production.tpr -o tmp3.xtc -fit rot+trans -n 1/aux.ndx   >& out || { cat out; exit 1; } ; mv tmp3.xtc pca.xtc  ; 
done

fi

pca_traj="pca100.xtc"

cd chol

{
 echo \"tetra1_BB\" \| \"tetra2_BB\" 
 echo q
 } | gmx make_ndx -f 1/confout.gro -n 1/aux.ndx -o two_tet.ndx

echo tetra1_BB tetra1_BB_tetra2_BB | gmx covar -f "$pca_traj" -s 1/production.tpr -n two_tet.ndx 
echo tetra1_BB tetra1_BB_tetra2_BB | gmx  anaeig -f "$pca_traj" -s 1/production.tpr -n two_tet.ndx  -extr -first 1 -last 3 -nframes 20 -3d  

rm \#*\#

cd $directory

cd no_chol

{
 echo \"tetra1_BB\" \| \"tetra2_BB\" 
 echo q
 } | gmx make_ndx -f 1/confout.gro -n 1/aux.ndx -o two_tet.ndx

echo tetra1_BB tetra1_BB_tetra2_BB | gmx anaeig -f "$pca_traj" -s 1/production.tpr  -n two_tet.ndx -extr -first 1 -last 3 -nframes 20 -3d -eig ../chol/eigenval.xvg -v ../chol/eigenvec.trr

rm \#*\#


