start_dir=$( pwd )

membranes=($( echo chol no_chol ))

for membrane in ${membranes[*]}
    do

	outdir=$( echo $start_dir/$membrane)
	cd $outdir
	pwd

	for rep in {1..10}
	do	
		cat $start_dir/top_template.top > $rep/topol.top
		echo "Protein_chain_A     8" >> $rep/topol.top
		echo "HOH                88" >> $rep/topol.top
		if [ $membrane =  chol ] ; then
			echo "PSMR               12" >> $rep/topol.top   # non_native
			echo "CHLR                2" >> $rep/topol.top   # non_native
		elif [ $membrane =  no_chol ] ; then
			echo "PSMR               14" >> $rep/topol.top
		fi
		
		grep "PSM " $rep/confout.gro | grep -c " P" | xargs -n1 -I{} sh -c 'echo "PSM   	         {}"' >> $rep/topol.top
		grep "SOL " $rep/confout.gro | grep -c " OW" | xargs -n1 -I{} sh -c 'echo "SOL   	         {}"' >> $rep/topol.top
		grep -c "NA " $rep/confout.gro  | xargs -n1 -I{} sh -c 'echo "NA   	         {}"' >> $rep/topol.top
		grep -c "CL " $rep/confout.gro  | xargs -n1 -I{} sh -c 'echo "CL   	         {}"' >> $rep/topol.top

		sed -i 's/HOH/SOL/g' $start_dir/$membrane/$rep/topol.top 
		sed -i 's/CHLR/CHL1/g' $start_dir/$membrane/$rep/topol.top 
		sed -i 's/PSMR/PSM /g' $start_dir/$membrane/$rep/topol.top

		grep -v CL $start_dir/$membrane/$rep/confout.gro | head -n -1 > $start_dir/$membrane/$rep/tmp.gro
		grep CL $start_dir/$membrane/$rep/confout.gro  >> $start_dir/$membrane/$rep/tmp.gro
		tail -n 1 $start_dir/$membrane/$rep/confout.gro >> $start_dir/$membrane/$rep/tmp.gro
		
		{
		if [ $membrane = chol ] ; then
		echo \"Protein\" \| r CHLR \| r PSMR \| r PSM
		elif [ $membrane = no_chol ] ; then
		echo \"Protein\" \| r PSMR \| r PSM
		fi
		echo r SOL \| r CL \| r NA \| r HOH
		echo q
		} | gmx make_ndx -f $start_dir/$membrane/$rep/tmp.gro -o $start_dir/$membrane/$rep/index_posre.ndx   >& out || { cat out; exit 1 ;}
		
		if [ $membrane = chol ] ; then
		sed -i 's/ Protein_CHLR_PSMR_PSM / MEMB /g' $start_dir/$membrane/$rep/index_posre.ndx
		elif [ $membrane = no_chol ] ; then
		sed -i 's/ Protein_PSMR_PSM / MEMB /g' $start_dir/$membrane/$rep/index_posre.ndx
		fi
		sed -i 's/ SOL_CL_NA_HOH / SOL_ION /g' $start_dir/$membrane/$rep/index_posre.ndx
		
		sed -i 's/PSMR/PSM /g' $start_dir/$membrane/$rep/tmp.gro
		sed -i 's/CHLR/CHL1/g' $start_dir/$membrane/$rep/tmp.gro

		gmx grompp -f $start_dir/step7_production.mdp -p $start_dir/$membrane/$rep/topol.top -c $start_dir/$membrane/$rep/tmp.gro  -n $start_dir/$membrane/$rep/index_posre.ndx  -o $start_dir/$membrane/$rep/production.tpr >& out || { cat out; exit 1 ;}

	done

    done
