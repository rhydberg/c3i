while read asc
do
printf '\'$(printf "%o" $asc) >> out
done
