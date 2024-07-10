start_dir=$( pwd )

membranes=($( echo chol no_chol ))

for membrane in ${membranes[*]}
    do
    
    outdir=$( echo $start_dir/$membrane)
	cd $outdir
	pwd

	for rep in {6..10} #{1..5}
	do	
    
    cat $start_dir/top_template.top > $rep/topol.top
    echo "Protein_chain_A     8" >> $rep/topol.top
    		echo "SOL                88" >> $rep/topol.top
		if [ $membrane =  chol ] ; then
			echo "PSM               12" >> $rep/topol.top   # non_native
			echo "CHL1                2" >> $rep/topol.top   # non_native
			grep "PSM " $rep/confout.gro | grep -c " P" | awk '{print $1-12}' | xargs -n1 -I{} sh -c 'echo "PSM   	         {}"' >> $rep/topol.top
		elif [ $membrane =  no_chol ] ; then
            grep "PSM " $rep/confout.gro | grep -c " P" | xargs -n1 -I{} sh -c 'echo "PSM   	         {}"' >> $rep/topol.top
		fi
    grep "SOL " $rep/confout.gro | grep -c " OW" | awk '{print $1-88}' | xargs -n1 -I{} sh -c 'echo "SOL   	         {}"' >> $rep/topol.top
    grep -c "NA      NA" $rep/confout.gro | xargs -n1 -I{} sh -c 'echo "NA    	         {}"' >> $rep/topol.top
    grep -c "CL      CL" $rep/confout.gro | xargs -n1 -I{} sh -c 'echo "CL    	         {}"' >> $rep/topol.top
    done #rep
    done #membrane
