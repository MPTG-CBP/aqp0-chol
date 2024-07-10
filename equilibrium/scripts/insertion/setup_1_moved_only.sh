# script to setup the different systems starting from the membed output conformations
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
	mkdir $start_dir/$system
	mkdir $outdir
	cd $outdir
	pwd
    
    

 
    #    if [ $system =  one-tet ] && [ $membrane = high-chol ] ; then
    
    
    
    
    
    if [ $system =  two-tet ] ; then
        
        inserted_struc_dir=$( echo /home/mptg/JD/aquaporin/aqp0_juan/2xtet_AA/$membrane )
        struc=$( echo 2xtet-em.gro ) 
        membrane_dir=$( echo /home/mptg/JD/aquaporin/WalzSimulations/cluster/two-tet/two-tet_pure/ )
        
    else # not two-tet 
        if [ $system =  one-tet ] ; then
            inserted_struc_dir=$( echo /home/mptg/JD/aquaporin/aqp0_juan/tet_AA/chol )
            struc=$( echo tet-em.gro ) 
        else
            inserted_struc_dir=$( echo /home/mptg/JD/aquaporin/aqp0_juan/2xtet_AA/chol/ )
            struc=$( echo 2xtet-em.gro ) 
        fi
        
        membrane_dir=$( echo /home/mptg/JD/aquaporin/WalzSimulations/cluster/$system/$system\_$membrane )

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
    } | gmx editconf -f $struc -n temp.ndx -o extractedpdb.pdb  -c -bt cubic  >& out || { cat out; exit 1 ;}
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
    tail -n 1 coord.xvg | awk '{print $2,$3,$4-0.3}' | xargs -n3 sh -c 'gmx editconf -f extractedpdb.pdb -center $1 $2 $3 -o conf_centered.pdb ' sh
    
    find ./conf_centered.pdb -type f -exec sed -i 's/CHL1/CHLR/g' \{\} \;
    find ./conf_centered.pdb -type f -exec sed -i 's/SOL/HOH/g' \{\} \;
    find ./conf_centered.pdb -type f -exec sed -i 's/PSM /PSMR/g' \{\} \;
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
    
    {
    grep CRYST1 reordered_membrane.pdb
    grep ATOM conf_centered.pdb
    grep ATOM reordered_membrane.pdb
    } > tet_patch_clashing.pdb
    
    # EXECUTIVE DECISION HERE: inserted prortein et al, not coupled with membrane because it needs group exception for energy and is also freezegrp, check mdp
    
    {
    if [ $membrane =  chol ] || [ $system =  one-tet ] ; then
    echo \"Protein\" \| r CHLR \| r PSMR \| r HOH  
    else
    if [ $membrane =  no_chol ] ; then
    echo \"Protein\" \| r PSMR \| r HOH
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
    } | gmx make_ndx -f tet_patch_clashing.pdb -o index_membed.ndx   >& out || { cat out; exit 1 ;}

    # fix index file names
    if [ $system =  only-memb ] ; then
    sed -i 's/ HOH_CHLR / PROTEIN_GMEMBED /g' index_membed.ndx
    elif [ $system =  one-tet ] ; then
    sed -i 's/ Protein_CHLR_PSMR_HOH / PROTEIN_GMEMBED /g' index_membed.ndx
    else #two tet
    if [ $membrane =  chol ] ; then
    sed -i 's/ Protein_CHLR_PSMR_HOH / PROTEIN_GMEMBED /g' index_membed.ndx
    elif [ $membrane =  no_chol ] ; then
    sed -i 's/ Protein_PSMR_HOH / PROTEIN_GMEMBED /g' index_membed.ndx
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
    else #two tet_A
    echo "Protein_chain_A     8" >> topol_membed.top
    echo "HOH                88" >> topol_membed.top
    if [ $membrane =  chol ] ; then
    echo "PSMR               12" >> topol_membed.top
    echo "CHLR                2" >> topol_membed.top
    elif [ $membrane =  no_chol ] ; then
    echo "PSMR               14" >> topol_membed.top
    fi
   
    fi
    
    if [ $membrane = high-chol ] || [ $membrane = med-chol ] ; then
    grep " CHL1" tet_patch_clashing.pdb | grep -c " C3 " | xargs -n1 -I{} sh -c 'echo "CHL1   	         {}"' >> topol_membed.top
    fi
    grep " PSM " tet_patch_clashing.pdb | grep -c "  P " | xargs -n1 -I{} sh -c 'echo "PSM   	         {}"' >> topol_membed.top
    grep " SOL " tet_patch_clashing.pdb | grep -c " OH2 " | xargs -n1 -I{} sh -c 'echo "SOL    	         {}"' >> topol_membed.top
    grep -c " NA " tet_patch_clashing.pdb | xargs -n1 -I{} sh -c 'echo "NA    	         {}"' >> topol_membed.top
    grep -c " CL " tet_patch_clashing.pdb | xargs -n1 -I{} sh -c 'echo "CL   	         {}"' >> topol_membed.top
    
    fi
    
    if true ; then
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
    echo "xyinit                   = 0.6500" >> membed.dat
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

