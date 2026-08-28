#!/bin/bash

#input
read -p "nhap ten cua ban: " name
read -p "nhap tuoi cua ban: " age
read -sp "nhap mat khau cua ban: " password
echo
echo "nhap vao day so yeu thich cua ban: "
read -a array

#output
echo "thong tin cua ban:"
echo "Ten: $name"
echo "Tuoi: $age"
echo "Mat khau: $password"
echo "Day so yeu thich: ${array[@]}"