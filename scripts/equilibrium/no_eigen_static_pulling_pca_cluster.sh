module load gromacs/2019.6

start_dir=$( pwd )

for rates in glacial slowest slower 
do

for cholesterol in no_chol chol
do 

cd $start_dir/$rates/$cholesterol

trajname=prot_all.xtc
trajout=fitted_pca.xtc
struc_file=init_prot.pdb
topo_file=production.tpr



{
echo a_1-13328_\&_r_9-32_r_39-61_r_68-78_r_85-107_r_127-147_r_160-176_r_184-194_r_201-219_\&_C-alpha
echo a_1-26656_\&_r_9-32_r_39-61_r_68-78_r_85-107_r_127-147_r_160-176_r_184-194_r_201-219_\&_C-alpha
} | gmx anaeig -f $trajout -s $topo_file -v /u/camiloap/JDOZ/AQP0/production/two-tet/no_chol/eigenvec.trr  -n pca.ndx  -extr -first 1 -last 3 -nframes 20 -3d 



done

done
