start_dir=$( pwd )

for system in one-tet-nolip # only-memb one-tet two-tet
do

    if [ $system = only-memb ] ; then
	membranes=($( echo high-chol  med-chol  pure ))
	
    else
    if [ $system =  one-tet ] ; then
	membranes=($( echo high-chol  med-chol  pure ))
    else # two-tet
	membranes=($( echo chol no_chol ))
    fi
fi

    for membrane in ${membranes[*]}
    do
    
    cp /home/mptg/JD/aquaporin/WalzSimulations/cluster/insertion/$system/$membrane/topol.top $start_dir/$system/$membrane/
	cp /home/mptg/JD/aquaporin/WalzSimulations/cluster/insertion/$system/$membrane/index_posre.ndx $start_dir/$system/$membrane/
    cp /home/mptg/JD/aquaporin/WalzSimulations/cluster/insertion/$system/$membrane/*.itp $start_dir/$system/$membrane/
    cp -r /home/mptg/JD/aquaporin/WalzSimulations/cluster/insertion/$system/$membrane/charmm36-nov2018.ff $start_dir/$system/$membrane/
    
    sed -i 's/HOH/SOL/g' $start_dir/$system/$membrane/topol.top 
    sed -i 's/CHLR/CHL1/g' $start_dir/$system/$membrane/topol.top 
    sed -i 's/PSMR/PSM /g' $start_dir/$system/$membrane/topol.top 
    
    for rep in {1..5}
    do

	outdir=$( echo $start_dir/$system/$membrane/$rep )
	
	cd $outdir
	pwd
    

    
	gmx grompp -f $start_dir/step7_production.mdp -p ../topol.top -c confout.gro  -n ../index_posre.ndx  -o production.tpr >& out || { cat out; exit 1 ;}
	
	done # replicas
	done #membranes
	done #system
