#!/bin/bash

date=$(date +"%d/%m/%y" --date="2 days")
py_path=$(find ~ -name 'finalV3.py')
run="python3 $py_path"

id=$1
pass=$2
row=$3
t=$4

$run $id $pass $row $t $date
