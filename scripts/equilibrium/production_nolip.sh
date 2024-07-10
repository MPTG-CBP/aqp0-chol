start_dir=$( pwd )

for system in one-tet-nolip # only-memb one-tet two-tet
do

    if [ $system = only-memb ] ; then
	membranes=($( echo high-chol  med-chol  pure ))
	
    else
    if [ $system =  one-tet ] ; then
	membranes=($( echo high-chol  med-chol  pure ))
	else
	if [ $system =  one-tet-nolip ] ; then
	membranes=($( echo high-chol  med-chol ))
	else
	if [ $system =  two-tet-native ] ; then
	membranes=($( echo chol ))
    else # two-tet
	membranes=($( echo chol no_chol ))
    fi
fi
fi
fi

    for membrane in ${membranes[*]}
    do
    
    cp /home/mptg/JD/aquaporin/WalzSimulations/cluster/insertion/$system/$membrane/*.itp $start_dir/$system/$membrane/
    cp -r /home/mptg/JD/aquaporin/WalzSimulations/cluster/insertion/$system/$membrane/charmm36-nov2018.ff $start_dir/$system/$membrane/
    
    if [ $system =  one-tet-nolip ] ; then
    
    for rep in {1..5}
    do    
    
    cd $start_dir/$system/$membrane/
    pwd
    
    cp /home/mptg/JD/aquaporin/WalzSimulations/cluster/insertion/$system/$membrane/topol$rep.top $start_dir/$system/$membrane/
	#cp /home/mptg/JD/aquaporin/WalzSimulations/cluster/insertion/$system/$membrane/index_posre.ndx $start_dir/$system/$membrane/
	
	    {
    if [ $system =  only-memb ] ; then
    if [ $membrane = high-chol ] || [ $membrane = med-chol ] ; then
    echo r CHLR \| r PSM \| r CHL1 
    elif [ $membrane = pure ] ; then
    echo r CHLR \| r PSM 
    fi
    
    elif [ $system =  one-tet ] ; then
    if [ $membrane = high-chol ] || [ $membrane = med-chol ] ; then
    echo \"Protein\" \| r CHLR \| r PSMR \| r PSM \| r CHL1 
    elif [ $membrane = pure ] ; then
    echo \"Protein\" \| r CHLR \| r PSMR \| r PSM
    fi
    
    elif [ $system =  one-tet-nolip ] ; then

    echo \"Protein\" \| r PSM \| r CHL1 

    
    else  # two tet
    if [ $membrane = chol ] ; then
    echo \"Protein\" \| r CHLR \| r PSMR \| r PSM
    elif [ $membrane = no_chol ] ; then
    echo \"Protein\" \| r PSMR \| r PSM
    fi
    fi
    echo r SOL \| r CL \| r NA \| r HOH
    echo q
    } | gmx make_ndx -f $rep/confout.gro -o index_posre$rep.ndx   >& out || { cat out; exit 1 ;}
    
        #fix index files names 
    if [ $system =  only-memb ] ; then
    if [ $membrane = high-chol ] || [ $membrane = med-chol ] ; then
    sed -i 's/ CHLR_PSM_CHL1 / MEMB /g' index_posre$rep.ndx
    elif [ $membrane = pure ] ; then
    sed -i 's/ CHLR_PSM / MEMB /g' index_posre$rep.ndx
    fi
    
    elif [ $system =  one-tet ] ; then
    if [ $membrane = high-chol ] || [ $membrane = med-chol ] ; then
    sed -i 's/ Protein_CHLR_PSMR_PSM_CHL1 / MEMB /g' index_posre$rep.ndx
    elif [ $membrane = pure ] ; then
    sed -i 's/ Protein_CHLR_PSMR_PSM / MEMB /g' index_posre$rep.ndx
    fi
    
    elif [ $system =  one-tet-nolip ] ; then

    sed -i 's/ Protein_PSM_CHL1 / MEMB /g' index_posre$rep.ndx

    
    
    else  # two tet
    if [ $membrane = chol ] ; then
    sed -i 's/ Protein_CHLR_PSMR_PSM / MEMB /g' index_posre$rep.ndx
    elif [ $membrane = no_chol ] ; then
    sed -i 's/ Protein_PSMR_PSM / MEMB /g' index_posre$rep.ndx
    fi
    fi
    

    sed -i 's/ SOL_CL_NA_HOH / SOL_ION /g' index_posre$rep.ndx
    
    
    sed -i 's/HOH/SOL/g' $start_dir/$system/$membrane/topol$rep.top 
    sed -i 's/CHLR/CHL1/g' $start_dir/$system/$membrane/topol$rep.top 
    sed -i 's/PSMR/PSM /g' $start_dir/$system/$membrane/topol$rep.top 


	outdir=$( echo $start_dir/$system/$membrane/$rep )
	
	cd $outdir
	pwd
    
    
    gmx grompp -f $start_dir/step7_production.mdp -p ../topol$rep.top -c confout.gro  -n ../index_posre$rep.ndx  -o production.tpr >& out || { cat out; exit 1 ;}
	
	done
	
	else
	
	cp /home/mptg/JD/aquaporin/WalzSimulations/cluster/insertion/$system/$membrane/topol.top $start_dir/$system/$membrane/
	cp /home/mptg/JD/aquaporin/WalzSimulations/cluster/insertion/$system/$membrane/index_posre.ndx $start_dir/$system/$membrane/
	

    
    sed -i 's/HOH/SOL/g' $start_dir/$system/$membrane/topol.top 
    sed -i 's/CHLR/CHL1/g' $start_dir/$system/$membrane/topol.top 
    sed -i 's/PSMR/PSM /g' $start_dir/$system/$membrane/topol.top 


	outdir=$( echo $start_dir/$system/$membrane/$rep )
	
	cd $outdir
	pwd
    
    
    
    for rep in {1..5}
    do
    
	gmx grompp -f $start_dir/step7_production.mdp -p ../topol.top -c confout.gro  -n ../index_posre.ndx  -o production.tpr >& out || { cat out; exit 1 ;}
	
	done # replicas
	
	fi
	
	done #membranes
	done #system
