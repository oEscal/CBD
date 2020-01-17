#! /bin/bash
# this script can be used to massive insertion of names (as keys) in redis

IFS=$'\n'

result="mset "
for name in $(cat female-names.txt); do
   result+="$name '' "
done

printf $result > female_names_keys.txt
echo Done
