#! /bin/bash

names_with_occ=$(cat nomes-registados-2018.csv | cut -d "," -f1,3)

result=""
for n in $(cat nomes-registados-2018.csv); do
   name=$(echo $n | cut -d "," -f1)
   number_occ=$(echo $n | cut -d "," -f3)
   result+=$(printf "*3\r\n\$3\r\nset\r\n\$${#name}\r\n$name\r\n\$${#number_occ}\r\n$number_occ\r\n")
done

printf "%s" $result > nomes_registados_redis.txt
echo DONE
#printf "*3\r\n\$5\r\nset\r\n\$4\r\nn%s\r\n\$3\r\n%s\r\n" $names_with_occ \
#      | sed "s/,/ /" > nomes_registados_redis.txt
#echo DONE