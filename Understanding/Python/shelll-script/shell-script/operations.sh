#!/bin/bash

#input a b
read -p "nhap so nhu nhat: " a
read -p "nhap so thu hai: " b

#tinh toan
tong=$(($a+$b))
echo "$a + $b = $tong"

let hieu=$a-$b
echo "$a - $b = $hieu"

echo "$a * $b = $(expr $a \* $b)"

echo "$a / $b = $(($a/$b))"