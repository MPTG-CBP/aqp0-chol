
start_dir=$( pwd )

for rate in slower slowest glacial
do 

for cholesterol in chol nochol
do

for rep in {1..10}
do

valorX=$( wc short_filter_$rate\_$cholesterol\_$rep\_x.txt | awk '{print $1}' )
valorF=$( wc short_filter_$rate\_$cholesterol\_$rep\_f.txt | awk '{print $1}' )

if [ "$valorX" -eq "$valorF" ]; then
  echo "They're equal"
  else
  echo $rate $cholesterol $rep
  echo $valorX $valorF
fi

done # rep

done #  cholesterol

done  # rate
