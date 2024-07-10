start_dir=$( pwd )

for system in  two-tet-native # one-tet-nolip only-memb one-tet two-tet
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
	membranes=($( echo chol no_chol ))
    else # two-tet
	membranes=($( echo chol no_chol ))
    fi
fi
fi 
fi

    for membrane in ${membranes[*]}
    do

	outdir=$( echo $start_dir/$system/$membrane)
	cd $outdir
	pwd

	
	
	
	
	
#	if [ $system =  one-tet ] && [ $membrane = high-chol ] ; then

	
	
	
    cat $start_dir/top_template.top > topol.top
    if [ $system =  only-memb ] ; then
    echo "HOH                 1" >> topol.top
    echo "CHLR                1" >> topol.top
    elif [ $system =  one-tet ] ; then
    echo "Protein_chain_A     4" >> topol.top
    echo "HOH                48" >> topol.top
    echo "PSMR               40" >> topol.top
    echo "CHLR               24" >> topol.top
    elif [ $system =  one-tet-nolip ] ; then
    echo "Protein_chain_A     4" >> topol.top 
    echo "HOH                48" >> topol.top 
    else #two tet_A
    echo "Protein_chain_A     8" >> topol.top
    echo "HOH                88" >> topol.top
    if [ $membrane =  chol ] ; then
    #echo "PSMR               12" >> topol_membed.top   # non_native
    #echo "CHLR                2" >> topol_membed.top   # non_native
    echo "PSMR               10" >> topol.top
    echo "CHLR                8" >> topol.top
    elif [ $membrane =  no_chol ] ; then
    echo "PSMR               14" >> topol.top
    echo "CHLR                2" >> topol.top  # only in native
    fi
    fi
    

    if [ $system =  one-tet-nolip ]  ; then
    
    for rep in {1..5}
    do
    
    cp topol.top topol$rep.top 
    
    if [ $membrane = high-chol ] || [ $membrane = med-chol ] ; then
    grep " CHL1" confout$rep.pdb | grep -c " C3 " | xargs -n1 -I{} sh -c 'echo "CHL1   	         {}"' >> topol$rep.top 
    fi
    grep " PSM " confout$rep.pdb | grep -c "  P " | xargs -n1 -I{} sh -c 'echo "PSM   	         {}"' >> topol$rep.top 
    grep " SOL " confout$rep.pdb | grep -c " OW " | xargs -n1 -I{} sh -c 'echo "SOL    	         {}"' >> topol$rep.top 
    grep -c " NA " confout$rep.pdb | xargs -n1 -I{} sh -c 'echo "NA    	         {}"' >> topol$rep.top 
    grep -c " CL " confout$rep.pdb | xargs -n1 -I{} sh -c 'echo "CL   	         {}"' >> topol$rep.top 
    
    
    {
    if [ $system =  only-memb ] ; then
    echo del 0-4
    else
    echo \"Protein\"
    echo del 0-15
    fi
    echo r SOL 
    echo q
    } | gmx make_ndx -f confout$rep.pdb -o help.ndx   >& out || { cat out; exit 1 ;}
    
    gmx grompp -f $start_dir/em.mdp -c confout$rep.pdb -p topol$rep.top  -n help.ndx -o tmp.tpr >& out || { cat out; exit 1 ;}

    {
    echo SOL
    } | gmx genion -s tmp.tpr -neutral -p topol$rep.top  -o system_neutral.gro -n help.ndx >& out || { cat out; exit 1 ;}

    gmx grompp -f $start_dir/em.mdp -p topol$rep.top  -c system_neutral.gro -o em.tpr >& out || { cat out; exit 1 ;}
    gmx mdrun -deffnm em -v >& out || { cat out; exit 1 ;}
    
    
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
    # echo \"Protein\" \| r PSMR \| r PSM   # non_native
    echo \"Protein\" \| r CHLR \| r PSMR \| r PSM
    fi
    fi
    echo r SOL \| r CL \| r NA \| r HOH
    echo q
    } | gmx make_ndx -f em.gro -o index_posre.ndx   >& out || { cat out; exit 1 ;}
    
    
    {
    echo System
    } | gmx trjconv -f em.gro -o em.pdb -s em.tpr  >& out || { cat out; exit 1 ;}
    
    #fix index files names 
    if [ $system =  only-memb ] ; then
    if [ $membrane = high-chol ] || [ $membrane = med-chol ] ; then
    sed -i 's/ CHLR_PSM_CHL1 / MEMB /g' index_posre.ndx
    elif [ $membrane = pure ] ; then
    sed -i 's/ CHLR_PSM / MEMB /g' index_posre.ndx
    fi
    
    elif [ $system =  one-tet ] ; then
    if [ $membrane = high-chol ] || [ $membrane = med-chol ] ; then
    sed -i 's/ Protein_CHLR_PSMR_PSM_CHL1 / MEMB /g' index_posre.ndx
    elif [ $membrane = pure ] ; then
    sed -i 's/ Protein_CHLR_PSMR_PSM / MEMB /g' index_posre.ndx
    fi
    
    elif [ $system =  one-tet-nolip ] ; then

    sed -i 's/ Protein_PSM_CHL1 / MEMB /g' index_posre.ndx

    
    
    else  # two tet
    if [ $membrane = chol ] ; then
    sed -i 's/ Protein_CHLR_PSMR_PSM / MEMB /g' index_posre.ndx
    elif [ $membrane = no_chol ] ; then
    # sed -i 's/ Protein_PSMR_PSM / MEMB /g' index_posre.ndx  # non_native
    sed -i 's/ Protein_CHLR_PSMR_PSM / MEMB /g' index_posre.ndx
    fi
    fi
    sed -i 's/ SOL_CL_NA_HOH / SOL_ION /g' index_posre.ndx


    mkdir $rep/
    
    gmx grompp -f $start_dir/posre_equilibration.mdp -p topol$rep.top  -c em.pdb -r em.pdb  -n index_posre.ndx  -o $rep/equilibration_posre.tpr >& out || { cat out; exit 1 ;}
    done
    
    
    
    
    
    
    else
    
        if [ $membrane = high-chol ] || [ $membrane = med-chol ] ; then
    grep " CHL1" confout.pdb | grep -c " C3 " | xargs -n1 -I{} sh -c 'echo "CHL1   	         {}"' >> topol.top
    fi
    if [ $membrane =  chol ] ; then
    grep " PSM " confout.pdb | grep -c "  P " | awk '{print $1-10}' | xargs -n1 -I{} sh -c 'echo "PSM   	         {}"' >> topol.top
    elif [ $membrane =  no_chol ] ;then
    grep " PSM " confout.pdb | grep -c "  P " | awk '{print $1-14}' | xargs -n1 -I{} sh -c 'echo "PSM   	         {}"' >> topol.top
    else
    grep " PSM " confout.pdb | grep -c "  P " | xargs -n1 -I{} sh -c 'echo "PSM   	         {}"' >> topol.top
    fi
    grep " SOL " confout.pdb | grep -c " OW " | awk '{print $1-88}' | xargs -n1 -I{} sh -c 'echo "SOL    	         {}"' >> topol.top
    grep -c " NA " confout.pdb | xargs -n1 -I{} sh -c 'echo "NA    	         {}"' >> topol.top
    grep -c " CL " confout.pdb | xargs -n1 -I{} sh -c 'echo "CL   	         {}"' >> topol.top
    
    
    {
    if [ $system =  only-memb ] ; then
    echo del 0-4
    else
    echo \"Protein\"
    echo del 0-15
    fi
    echo r SOL 
    echo q
    } | gmx make_ndx -f confout.pdb -o help.ndx   >& out || { cat out; exit 1 ;}
    
    gmx grompp -f $start_dir/em.mdp -c confout.pdb -p topol.top -n help.ndx -o tmp.tpr >& out || { cat out; exit 1 ;}

    {
    echo SOL
    } | gmx genion -s tmp.tpr -neutral -p topol.top -o system_neutral.gro -n help.ndx >& out || { cat out; exit 1 ;}

    gmx grompp -f $start_dir/em.mdp -p topol.top -c system_neutral.gro -o em.tpr >& out || { cat out; exit 1 ;}
    gmx mdrun -deffnm em -v >& out || { cat out; exit 1 ;}
    
    
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
    
    else  # two tet
    if [ $membrane = chol ] ; then
    echo \"Protein\" \| r CHLR \| r PSMR \| r PSM
    elif [ $membrane = no_chol ] ; then
    #echo \"Protein\" \| r PSMR \| r PSM  # for non_native
    echo \"Protein\" \| r CHLR \| r PSMR \| r PSM
    fi
    fi
    echo r SOL \| r CL \| r NA \| r HOH
    echo q
    } | gmx make_ndx -f em.gro -o index_posre.ndx   >& out || { cat out; exit 1 ;}
    
    
    {
    echo System
    } | gmx trjconv -f em.gro -o em.pdb -s em.tpr  >& out || { cat out; exit 1 ;}
    
    #fix index files names 
    if [ $system =  only-memb ] ; then
    if [ $membrane = high-chol ] || [ $membrane = med-chol ] ; then
    sed -i 's/ CHLR_PSM_CHL1 / MEMB /g' index_posre.ndx
    elif [ $membrane = pure ] ; then
    sed -i 's/ CHLR_PSM / MEMB /g' index_posre.ndx
    fi
    
    elif [ $system =  one-tet ] ; then
    if [ $membrane = high-chol ] || [ $membrane = med-chol ] ; then
    sed -i 's/ Protein_CHLR_PSMR_PSM_CHL1 / MEMB /g' index_posre.ndx
    elif [ $membrane = pure ] ; then
    sed -i 's/ Protein_CHLR_PSMR_PSM / MEMB /g' index_posre.ndx
    fi
    
    else  # two tet
    if [ $membrane = chol ] ; then
    sed -i 's/ Protein_CHLR_PSMR_PSM / MEMB /g' index_posre.ndx
    elif [ $membrane = no_chol ] ; then
    #sed -i 's/ Protein_PSMR_PSM / MEMB /g' index_posre.ndx   # for non_native
    sed -i 's/ Protein_CHLR_PSMR_PSM / MEMB /g' index_posre.ndx
    fi
    fi
    sed -i 's/ SOL_CL_NA_HOH / SOL_ION /g' index_posre.ndx

    for i in {1..5} 
    do
    mkdir $i/
    gmx grompp -f $start_dir/posre_equilibration.mdp -p topol.top -c em.pdb -r em.pdb  -n index_posre.ndx  -o $i/equilibration_posre.tpr >& out || { cat out; exit 1 ;}
    done
    
    fi
    
    
    
    

    
    done # loop over membranes
done # loop over systems
