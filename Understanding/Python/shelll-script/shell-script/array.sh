#!/bin/bash

<<COMMENT
tính tổng các số nhập vào từ bàng phím
COMMENT

# nhập vào mảng
read -p "nhập các số, các số cách nhau bởi dấu <space>: " -a arr

# số lượng phần tử trong mảng
n=${#arr[@]}

# khởi tọa một biến tổng
tong=0

# tính tổng các số trong mảng
for ((i=0;i<n;i++)); do
	tong=$((tong + ${arr[$i]}))
done

# hiểm thị kết quả
echo "tổng của các số trong mảng là: $tong";
