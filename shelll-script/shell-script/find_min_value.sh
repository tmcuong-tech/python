#!/bin/bash

# nhap mang
read -p "nhap cac so cach nhau boi dau <space>: " -a arr

# so luong phan tu cua mang
n=${#arr[@]}

# hien thi mang
echo "mang: ${arr[@]}"

# tao gia tri nho nhat
min=${arr[0]}

# tim kiem
for i in "${arr[@]}"; do
	if [ $i -lt $min ]; then
		min=$i
	fi
done

# in ket qua
echo "gia tri nho nhat trong mang: $min"
