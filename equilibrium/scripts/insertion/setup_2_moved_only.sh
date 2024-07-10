start_dir=$( pwd )

for system in only-memb # one-tet two-tet
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

	outdir=$( echo $start_dir/$system/$membrane)
	cd $outdir
	pwd
	
	#cat PSM_posres.itp > PSMP_posres.itp
	cat PSM.itp > PSMP_posres.itp
	
	#sed -i 's/PSMR/PSMP/g' PSMP_posres.itp
    sed -i 's/PSM/PSMP/g' PSMP_posres.itp

	cat << 'EOF' >> PSMP_posres.itp
; Include Position restraint file
#ifdef POSRES_PLIPID
#include "posre_PSMP.itp"
#endif
EOF



cat << 'EOF' > posre_PSMP.itp
[ position_restraints ]
; atom  type      fx      fy      fz
    20     1     0     0   100
EOF


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
    else #two tet_A
    echo "Protein_chain_A     8" >> topol.top
    echo "HOH                88" >> topol.top
    if [ $membrane =  chol ] ; then
    echo "PSMR               12" >> topol.top
    echo "CHLR                2" >> topol.top
    elif [ $membrane =  no_chol ] ; then
    echo "PSMR               14" >> topol.top
    fi
    fi
    
    if [ $membrane = high-chol ] || [ $membrane = med-chol ] ; then
    grep " CHL1" confout.pdb | grep -c " C3 " | xargs -n1 -I{} sh -c 'echo "CHL1   	         {}"' >> topol.top
    fi
    
    if [ $system =  only-memb ] ; then
    grep " PSM " confout.pdb | awk '{if($3=="P" && $8>51) print $0}' | grep -c "  P " | xargs -n1 -I{} sh -c 'echo "PSM   	         {}"' >> topol.top
    grep " PSM " confout.pdb | awk '{if($3=="P" && $8<51) print $0}' | grep -c "  P " | xargs -n1 -I{} sh -c 'echo "PSMP  	         {}"' >> topol.top
    else
    grep " PSM " confout.pdb | grep -c "  P " | xargs -n1 -I{} sh -c 'echo "PSM   	         {}"' >> topol.top
    fi
    
    grep " SOL " confout.pdb | grep -c " OW " | xargs -n1 -I{} sh -c 'echo "SOL    	         {}"' >> topol.top
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
    echo r CHLR \| r PSM \| r CHL1 \| r PSMP
    elif [ $membrane = pure ] ; then
    echo r CHLR \| r PSM \| r PSMP
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
    echo \"Protein\" \| r PSMR \| r PSM
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
    sed -i 's/ CHLR_PSM_CHL1_PSMP / MEMB /g' index_posre.ndx
    elif [ $membrane = pure ] ; then
    sed -i 's/ CHLR_PSM_PSMP / MEMB /g' index_posre.ndx
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
    sed -i 's/ Protein_PSMR_PSM / MEMB /g' index_posre.ndx
    fi
    fi
    sed -i 's/ SOL_CL_NA_HOH / SOL_ION /g' index_posre.ndx

    for i in {1..5} 
    do
    mkdir $i/
    gmx grompp -f $start_dir/posre_equilibration.mdp -p topol.top -c em.pdb -r em.pdb  -n index_posre.ndx  -o $i/equilibration_posre.tpr >& out || { cat out; exit 1 ;}
    done
    
    done # loop over membranes
done # loop over systems
