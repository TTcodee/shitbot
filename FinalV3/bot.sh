#!/bin/bash
day=$(date "+%d")
day=$[$day+2]
month_and_year=$(date "+%m/%y")
date=$(echo $day $month_and_year | awk '{printf("%s/%s"), $1, $2}')
# run=$(find ~ -type f -name 'finalV2')
run="python3 finalV3.py"

# echo "User ID:"
# read id
# echo "Password:"
# read pass
# echo "row:"
# read row
# echo "time://17:00 = 1, 18:00 = 2, 19:00 = 3, 20:00 = 4"
# read t
id=$1
pass=$2
row=$3
t=$4

$run $id $pass $row $t $date
