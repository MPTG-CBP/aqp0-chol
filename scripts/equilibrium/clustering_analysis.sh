
pwd

cd ~/JD/aquaporin/WalzSimulations/cluster/one-tet/one-tet_high-chol 

/home/mptg/Downloads/gromacs/build/bin/gmx maptide -f traj_comp.xtc -s confout.pdb -select 'resname CHL1' -margin 5 -mo before_insertion_100ns.ccp4 -b 400000

for rep in {1..5}
do

cd ~/JD/aquaporin/WalzSimulations/whole-system/one-tet/high-chol/$rep

gmx editconf -f confout.gro -o confout.pdb

/home/mptg/Downloads/gromacs/build/bin/gmx maptide -f traj_comp.xtc -s confout.pdb -select 'resname CHL1' -margin 5 -mo after_insertion_$rep.ccp4 -e 100000 -b 0

done
