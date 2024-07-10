start_dir=$( pwd )

for rate in slower slowest glacial
do

for lip in chol no_chol
do

for rep in {1..20}   # {1..10}
do
cd $start_dir/$rate/$lip/$rep

len_pullx=$( grep -E -v '^@|^#'  pullx.xvg | awk '{if(NF==2) print $0}' | wc -l  )
len_pullf=$( grep -E -v '^@|^#'  pullf.xvg | awk '{if(NF==2) print $0}' | wc -l  )

minor_len=$(( len_pullx < len_pullf ? len_pullx : len_pullf ))

grep -E -v '^@|^#'  pullx.xvg | awk '{if(NF==2) print $0}' | head -n $minor_len > pullx_format.xvg 
grep -E -v '^@|^#'  pullf.xvg | awk '{if(NF==2) print $0}' | head -n $minor_len > pullf_format.xvg 

done #rep
done #lip
done #rate 
