#!/bin/bash

# khai bao file
file_input="$1"
file_output="$2"

# kiem tra file input
if [ ! -f "$file_input" ]; then
    echo "$file_input khong ton tai"
    exit
fi

# doc mang tu file
read -r -a arr < "$file_input"

# lay so luong phan tu
n=${#arr[@]}

# sap xep tang dan (bubble sort)
for ((i=0; i<n-1; i++)); do
    for ((j=i+1; j<n; j++)); do

        if [ ${arr[j]} -lt ${arr[i]} ]; then
            temp=${arr[i]}
            arr[i]=${arr[j]}
            arr[j]=$temp
        fi

    done
done

# xuat ket qua ra file
echo "${arr[@]}" > "$file_output"

echo "Sap xep thanh cong!"
echo "Ket qua da luu vao: $file_output"
