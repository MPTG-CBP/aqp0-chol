# script to setup the different systems starting from the membed output conformations
start_dir=$( pwd )

for system in two-tet-native  # one-tet-nolip only-memb one-tet two-tet
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
	#membranes=($( echo chol  no_chol ))
	membranes=($( echo no_chol )) # test, delete later
    else # two-tet
	membranes=($( echo chol ))
    fi
    fi
fi
fi

    for membrane in ${membranes[*]}
    do

	outdir=$( echo $start_dir/$system/$membrane)
	mkdir $start_dir/$system
	mkdir $outdir
	cd $outdir
	pwd
    
    

 
    #    if [ $system =  one-tet ] && [ $membrane = high-chol ] ; then
    
    
    
    
    
    if [ $system =  two-tet ] ; then
        
        inserted_struc_dir=$( echo /home/mptg/JD/aquaporin/aqp0_juan/2xtet_AA/$membrane )
        struc=$( echo 2xtet-em.gro ) 
        membrane_dir=$( echo /home/mptg/JD/aquaporin/WalzSimulations/cluster/two-tet/two-tet_pure/ )
    elif [ $system =  two-tet-native ] ; then
        
        # FIX FIX FIX FIX FIX FIX FIX FIX FIX 
        
        inserted_struc_dir=$( echo /home/mptg/JD/aquaporin/aqp0_juan/2xtet_native/$membrane\2 )  
        echo $inserted_struc_dir
        struc=$( echo 2xtet-em.gro ) 
        membrane_dir=$( echo /home/mptg/JD/aquaporin/WalzSimulations/cluster/two-tet/two-tet_pure/ )
    
        
    else # not two-tet 
        if [ $system =  one-tet ] || [ $system =  one-tet-nolip ]; then
            inserted_struc_dir=$( echo /home/mptg/JD/aquaporin/aqp0_juan/tet_AA/chol )
            struc=$( echo tet-em.gro ) 
            membrane_dir=$( echo /home/mptg/JD/aquaporin/WalzSimulations/cluster/one-tet/one-tet_$membrane )
        else
            inserted_struc_dir=$( echo /home/mptg/JD/aquaporin/aqp0_juan/2xtet_AA/chol/ )
            struc=$( echo 2xtet-em.gro ) 
            membrane_dir=$( echo /home/mptg/JD/aquaporin/WalzSimulations/cluster/$system/$system\_$membrane )
        fi
    fi
    
    if true; then

    cp $inserted_struc_dir/*.itp .
    cp $inserted_struc_dir/*.top .
    cp -r $inserted_struc_dir/charmm36-nov2018.ff .
    cp  $inserted_struc_dir/$struc .
    cp $membrane_dir/confout.gro  ./membrane.gro
    cp $membrane_dir/step7_production.tpr  .
    
    if [ $system = only-memb ] ; then
    {
    echo splitres 17
    echo r 231
    echo 18 \| 20
    echo q
    } | gmx make_ndx -f $struc -o temp.ndx  >& out || { cat out; exit 1 ;}
    {   
    echo System
    echo CHL1_CHL1_325_r_231
    } | gmx editconf -f $struc -n temp.ndx -o extractedpdb.pdb  -c  -bt cubic  >& out || { cat out; exit 1 ;}
    else
    {
    echo System
    echo System
    } | gmx editconf -f $struc -o extractedpdb.pdb  -c  -bt cubic  >& out || { cat out; exit 1 ;}
    fi
    
    mv topol.top old_topol.top
    
    {
    echo System
    } | gmx trjconv -f membrane.gro -o membrane.pdb -s step7_production.tpr  >& out || { cat out; exit 1 ;}
    
    {
    echo System
    } | gmx traj -f membrane.pdb -s membrane.pdb -ox -com
    
    tail -n 1 coord.xvg | awk '{print $2,$3,$4}' | xargs -n3 sh -c 'gmx editconf -f extractedpdb.pdb -center $1 $2 $3 -o conf_centered.pdb ' sh  >& out || { cat out; exit 1 ;}
    
    find ./conf_centered.pdb -type f -exec sed -i 's/CHL1/CHLR/g' \{\} \;
    find ./conf_centered.pdb -type f -exec sed -i 's/SOL/HOH/g' \{\} \;
    find ./conf_centered.pdb -type f -exec sed -i 's/PSM /PSMR/g' \{\} \;
    
    if [ $system =  one-tet-nolip ] ; then
    
    grep -e 'CHL1' -e 'PSM' -v extractedpdb.pdb > extractedpdb_nolip.pdb
    
    gmx editconf -f extractedpdb_nolip.pdb -rotate 0 0 18 -o extractedpdb1.pdb
    gmx editconf -f extractedpdb_nolip.pdb -rotate 0 0 36 -o extractedpdb2.pdb
    gmx editconf -f extractedpdb_nolip.pdb -rotate 0 0 54 -o extractedpdb3.pdb
    gmx editconf -f extractedpdb_nolip.pdb -rotate 0 0 72 -o extractedpdb4.pdb
    gmx editconf -f extractedpdb_nolip.pdb -rotate 0 0 90 -o extractedpdb5.pdb
    
    for rep in {1..5}
    do
    
    tail -n 1 coord.xvg | awk '{print $2,$3,$4}' | xargs -n3 sh -c 'gmx editconf -f extractedpdb'$rep'.pdb -center $1 $2 $3 -o conf_centered'$rep'.pdb ' sh  >& out || { cat out; exit 1 ;}
    
    find ./conf_centered$rep.pdb -type f -exec sed -i 's/CHL1/CHLR/g' \{\} \;
    find ./conf_centered$rep.pdb -type f -exec sed -i 's/SOL/HOH/g' \{\} \;
    find ./conf_centered$rep.pdb -type f -exec sed -i 's/PSM /PSMR/g' \{\} \;
    
    done
    fi
    
    find ./membrane.pdb -type f -exec sed -i 's/CLA /CL  /g' \{\} \;
    find ./membrane.pdb -type f -exec sed -i 's/SOD /NA  /g' \{\} \;
    find ./membrane.pdb -type f -exec sed -i 's/TIP3/SOL /g' \{\} \;

    {
    grep CRYST1 membrane.pdb
    grep CHL1 membrane.pdb
    grep PSM membrane.pdb
    grep SOL membrane.pdb
    grep NA membrane.pdb
    grep CL membrane.pdb
    } > reordered_membrane.pdb
    
    
    #if [ $system =  one-tet-nolip ] ; then    
    #else
    #fi
    
    
    if [ $system =  one-tet-nolip ] ; then
    

    
    for rep in {1..5}
    do
    {
    grep CRYST1 reordered_membrane.pdb
    grep ATOM conf_centered$rep.pdb
    grep ATOM reordered_membrane.pdb
    } > tet_patch_clashing$rep.pdb
    done
    
    else
    
    {
    grep CRYST1 reordered_membrane.pdb
    grep ATOM conf_centered.pdb
    grep ATOM reordered_membrane.pdb
    } > tet_patch_clashing.pdb
    
    fi
    
    
    # EXECUTIVE DECISION HERE: inserted prortein et al, not coupled with membrane because it needs group exception for energy and is also freezegrp, check mdp
    
    if [ $system =  one-tet-nolip ] ; then
    tet_patch_clashing=$( echo tet_patch_clashing1.pdb ) 
    else
    tet_patch_clashing=$( echo tet_patch_clashing.pdb ) 
    fi
    
    
    {
    if [ $system =  one-tet-nolip ] ; then
    echo \"Protein\" \| r HOH  
    else
    if [ $membrane =  chol ] || [ $system =  one-tet ] ; then
    echo \"Protein\" \| r CHLR \| r PSMR \| r HOH  
    else
    if [ $membrane =  no_chol ] ; then
    echo \"Protein\" \| r CHLR \| r PSMR \| r HOH  #  for native
    #echo \"Protein\" \| r PSMR \| r HOH  # for non_native
    fi
    fi
    fi
    
    if [ $system =  only-memb ] ; then
    echo r HOH \| r CHLR
    fi
    
    if [ $membrane = high-chol ] || [ $membrane = med-chol ] ; then
    echo r CHL1 \| r PSM
    else
    if [ $membrane = pure ] ; then
    echo r PSM
    fi
    fi
    echo r PSM
    echo r SOL \| r CL \| r NA
    echo q
    } | gmx make_ndx -f $tet_patch_clashing -o index_membed.ndx   >& out || { cat out; exit 1 ;}

    # fix index file names
    if [ $system =  only-memb ] ; then
    sed -i 's/ HOH_CHLR / PROTEIN_GMEMBED /g' index_membed.ndx
    elif [ $system =  one-tet ] ; then
    sed -i 's/ Protein_CHLR_PSMR_HOH / PROTEIN_GMEMBED /g' index_membed.ndx
    elif [ $system =  one-tet-nolip ] ; then
    sed -i 's/ Protein_HOH / PROTEIN_GMEMBED /g' index_membed.ndx
    else #two tet
    if [ $membrane =  chol ] ; then
    sed -i 's/ Protein_CHLR_PSMR_HOH / PROTEIN_GMEMBED /g' index_membed.ndx
    elif [ $membrane =  no_chol ] ; then
    #sed -i 's/ Protein_PSMR_HOH / PROTEIN_GMEMBED /g' index_membed.ndx  # for non_native
    sed -i 's/ Protein_CHLR_PSMR_HOH / PROTEIN_GMEMBED /g' index_membed.ndx   # for native
    fi
    sed -i '0,/ PSM / s/ PSM / MEMBRANE /' index_membed.ndx
    fi
    
    if [ $membrane = high-chol ] || [ $membrane = med-chol ] ; then
    sed -i 's/ CHL1_PSM / MEMBRANE /g' index_membed.ndx
    elif [ $membrane = pure ] ; then
    sed -i '0,/ PSM / s/ PSM / MEMBRANE /' index_membed.ndx
    fi
    
    sed -i 's/ SOL_CL_NA / WATER_IONS /g' index_membed.ndx


    cat $start_dir/top_template.top > topol_membed.top
    if [ $system =  only-memb ] ; then
    echo "HOH                 1" >> topol_membed.top
    echo "CHLR                1" >> topol_membed.top
    elif [ $system =  one-tet ] ; then
    echo "Protein_chain_A     4" >> topol_membed.top
    echo "HOH                48" >> topol_membed.top
    echo "PSMR               40" >> topol_membed.top
    echo "CHLR               24" >> topol_membed.top
    elif [ $system =  one-tet-nolip ] ; then
    echo "Protein_chain_A     4" >> topol_membed.top
    echo "HOH                48" >> topol_membed.top
    else #two tet_A
    echo "Protein_chain_A     8" >> topol_membed.top
    echo "HOH                88" >> topol_membed.top
    if [ $membrane =  chol ] ; then
    #echo "PSMR               12" >> topol_membed.top   # non_native
    #echo "CHLR                2" >> topol_membed.top   # non_native
    echo "PSMR               10" >> topol_membed.top
    echo "CHLR                8" >> topol_membed.top
    elif [ $membrane =  no_chol ] ; then
    echo "PSMR               14" >> topol_membed.top
    echo "CHLR                2" >> topol_membed.top  # only in native
    fi
   
    fi
    
    if [ $membrane = high-chol ] || [ $membrane = med-chol ] ; then
    grep " CHL1" $tet_patch_clashing | grep -c " C3 " | xargs -n1 -I{} sh -c 'echo "CHL1   	         {}"' >> topol_membed.top
    fi
    grep " PSM " $tet_patch_clashing | grep -c "  P " | xargs -n1 -I{} sh -c 'echo "PSM   	         {}"' >> topol_membed.top
    grep " SOL " $tet_patch_clashing | grep -c " OH2 " | xargs -n1 -I{} sh -c 'echo "SOL    	         {}"' >> topol_membed.top
    grep -c " NA " $tet_patch_clashing | xargs -n1 -I{} sh -c 'echo "NA    	         {}"' >> topol_membed.top
    grep -c " CL " $tet_patch_clashing | xargs -n1 -I{} sh -c 'echo "CL   	         {}"' >> topol_membed.top
    
    fi
    
    
    
    
    
    if [ $system =  one-tet-nolip ] ; then
    
        cat << EOF > membed.dat   # check if tehy're all the same
nxy                      = 1000
nz                       = 0
xyend                    = 1.000000
zinit                    = 1.000000
zend                     = 1.000000
maxwarn                  = 1
xyinit                   = 0.8500
EOF
    
    
    for rep in {1..5}
    do
    
    gmx grompp -f $start_dir/g_membed.mdp -p topol_membed.top -c tet_patch_clashing$rep.pdb -n index_membed.ndx  -o membed$rep.tpr   -maxwarn 3   >& out || { cat out; exit 1 ;}
    
    {
    echo PROTEIN_GMEMBED
    echo MEMBRANE
    } | gmx mdrun -membed membed.dat -s membed$rep.tpr -mn index_membed.ndx  -v -c confout$rep.pdb  >& out || { cat out; exit 1 ;}
    
    done
    
    else
    
    gmx grompp -f $start_dir/g_membed.mdp -p topol_membed.top -c tet_patch_clashing.pdb -n index_membed.ndx  -o membed.tpr   -maxwarn 3   >& out || { cat out; exit 1 ;}
    
    cat << EOF > membed.dat   # check if tehy're all the same
nxy                      = 1000
nz                       = 0
xyend                    = 1.000000
zinit                    = 1.000000
zend                     = 1.000000
maxwarn                  = 1
EOF

    if [ $system =  only-memb ] && [ $membrane = med-chol ] ; then
    echo "xyinit                   = 0.4000" >> membed.dat
    elif [ $system =  only-memb ] && [ $membrane = pure ] ; then
    echo "xyinit                   = 0.7000" >> membed.dat
    else
    echo "xyinit                   = 0.8500" >> membed.dat
    fi
    
    {
    echo PROTEIN_GMEMBED
    echo MEMBRANE
    } | gmx mdrun -membed membed.dat -s membed.tpr -mn index_membed.ndx  -v -c confout.pdb  >& out || { cat out; exit 1 ;}
    
    fi
    
    
    
    
    #fi

    
    done # loop over membranes
done # loop over systems

