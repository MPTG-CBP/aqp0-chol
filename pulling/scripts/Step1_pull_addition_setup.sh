start_dir=$( pwd )

membranes=($( echo chol no_chol ))


#<<'END_COMMENT'

for membrane in ${membranes[*]}
    do


	for rep in {6..10} #{1..5}
	do	
    outdir=$( echo $start_dir/$membrane/$rep)
	cd $outdir
	
	pwd
	
	echo  System | gmx trjconv -s production.tpr -f traj_comp.xtc -o tmp1.pdb -dump 500000 
	echo  Protein Protein System | gmx trjconv -s production.tpr -f tmp1.pdb -o tmp2.pdb -center -ur compact -pbc cluster
	echo Protein System  | gmx trjconv -s production.tpr -f tmp2.pdb -o init500.pdb -center -ur compact -pbc mol
	
	echo  System | gmx trjconv -s production.tpr -f traj_comp.xtc -o tmp1.pdb -dump 750000 
	echo  Protein Protein System | gmx trjconv -s production.tpr -f tmp1.pdb -o tmp2.pdb -center -ur compact -pbc cluster
	echo Protein System  | gmx trjconv -s production.tpr -f tmp2.pdb -o init750.pdb -center -ur compact -pbc mol
	
	rm *tmp*pdb*
	
	done  #rep

    done  #membrane

    
#END_COMMENT

for membrane in chol
    do

	for rep in 6 8   # to replace replica 7 of chol that presented chol flip flop
	do	
    outdir=$( echo $start_dir/$membrane/$rep)
	cd $outdir
	
	pwd
	
	echo  System | gmx trjconv -s production.tpr -f traj_comp.xtc -o tmp1.pdb -dump 1000000 
	echo  Protein Protein System | gmx trjconv -s production.tpr -f tmp1.pdb -o tmp2.pdb -center -ur compact -pbc cluster
	echo Protein System  | gmx trjconv -s production.tpr -f tmp2.pdb -o init1000.pdb -center -ur compact -pbc mol

	rm *tmp*pdb*
	
	done  #rep

    done  #membrane
