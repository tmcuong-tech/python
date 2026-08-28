#!/bin/bash

# hàm kiểm tra số nguyên tố
isPrime() {
	n=$1

	# kiểm tra n <= 1
	if [ "$n" -le 1 ]; then
		echo "$n không phải là số nguyên tố."
        	return
    	fi
	
	# tính căn bậc 2 của n
	sqrt_n=$(awk "BEGIN {printf \"%d\", sqrt($n)}")

	# kiểm tra từ 2 đến √n
    	for ((i=2; i<=sqrt_n; i++)); do
        	if [ $((n % i)) -eq 0 ]; then
            		echo "$n không phải là số nguyên tố."
        		return
        	fi
    	done

	# nếu không chia hết
	echo "$n là số nguyên tố."
}

# nhập số
read -p "nhập số cần kiểm tra: " number

# gọi hàm
isPrime $number
