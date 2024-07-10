#source /usr/local/gromacs/bin/GMXRC

#source
start_dir=$( pwd )

membranes=($( echo chol no_chol ))

for membrane in ${membranes[*]}
    do
    


	for rep in {6..10} #{1..5}
	do	
    
    outdir=$( echo $start_dir/$membrane/$rep)
	cd $outdir
	pwd
	
    	{
		echo del 5-25
		echo \"Protein\" \| r PSM \| r CHL1
		echo name 5 MEMB
		echo r CL \|  r NA \| r SOL  
		echo name 6 SOL_ION
		echo r 9-28 \| r 37-55 \| r 69-77 \| r 83-106 \| r 127-148 \| r 161-175 \| r 185-193 \| r 203-217 \& \"Backbone\" \& a 1-13328
		echo name 7 Tetra1
		echo r 9-28 \| r 37-55 \| r 69-77 \| r 83-106 \| r 127-148 \| r 161-175 \| r 185-193 \| r 203-217 \& \"Backbone\" \& a 13329-26656
		echo name 8 Tetra2
		echo q
		} | gmx make_ndx -f confout.gro #  >& out || { cat out; exit 1 ;}
    
    
    
    rm \#*\#
    
    done #rep
    done #membrane
    
    cd $start_dir
    
    mkdir pulling_tpr
    
    for rate in slower slowest glacial
    do
    
    mkdir pulling_tpr/$rate
    
    for membrane in ${membranes[*]}
    do
    
    mkdir pulling_tpr/$rate/$membrane

	for rep in {6..10} #{1..5}
	do	
    
    initfiles=$( echo $start_dir/$membrane/$rep )
    outdir=$( echo pulling_tpr/$rate/$membrane/$[$rep+5] )   # for {6..10}
    # outdir=$( echo pulling_tpr/$rate/$membrane/$rep )  # {1..5}
    mkdir $outdir
    #cd $outdir
    
	gmx grompp -f $start_dir/pulling_$rate.mdp -p $initfiles/topol.top -c $initfiles/init500.pdb  -n $initfiles/index.ndx  -o $outdir/$rate.tpr  #>& out || { cat out; exit 1 ;}
    rm $outdir/\#*\#
    
    outdir=$( echo pulling_tpr/$rate/$membrane/$[$rep+10] )  # {6..10}
    # outdir=$( echo pulling_tpr/$rate/$membrane/$[$rep+5] )  # {1..5}
    mkdir $outdir
    #cd $outdir
    gmx grompp -f $start_dir/pulling_$rate.mdp -p $initfiles/topol.top -c $initfiles/init750.pdb  -n $initfiles/index.ndx  -o $outdir/$rate.tpr
    rm $outdir/\#*\#
    
    done #rep
    done #membrane
	
	done #rate 
	
	
	# fix to replacw replica 7 that presents chgol flip flop
	
    for rate in slower slowest glacial
    do
    
    mkdir pulling_tpr/$rate
    
    for membrane in chol
    do
    
    mkdir pulling_tpr/$rate/$membrane

	#for rep in 7
	for rep in 7
	do	
    
    #initfiles=$( echo $start_dir/$membrane/6 )
    initfiles=$( echo $start_dir/$membrane/$rep )    #?
    outdir=$( echo pulling_tpr/$rate/$membrane/$[$rep+5] )   # for {6..10}
    # outdir=$( echo pulling_tpr/$rate/$membrane/$rep )  # {1..5}
    mkdir $outdir
    #cd $outdir
    
	gmx grompp -f $start_dir/pulling_$rate.mdp -p $initfiles/topol.top -c $initfiles/init1000.pdb  -n $initfiles/index.ndx  -o $outdir/$rate.tpr  #>& out || { cat out; exit 1 ;}
    rm $outdir/\#*\#
    
    #initfiles=$( echo $start_dir/$membrane/8 )
    initfiles=$( echo $start_dir/$membrane/$rep )   #?
    outdir=$( echo pulling_tpr/$rate/$membrane/$[$rep+10] )  # {6..10}
    # outdir=$( echo pulling_tpr/$rate/$membrane/$[$rep+5] )  # {1..5}
    mkdir $outdir
    #cd $outdir
    gmx grompp -f $start_dir/pulling_$rate.mdp -p $initfiles/topol.top -c $initfiles/init1000.pdb  -n $initfiles/index.ndx  -o $outdir/$rate.tpr
    rm $outdir/\#*\#
    
    done #rep
    done #membrane
	
	done #rate 
