<<COMMENT
in ra bảng cửu chương
in ra tất cả bảng cửu chương
chuyển số thập phân sang số nhị phân
COMMENT

<<COMMENT
# in ra bảng cửu chương
# chọn bảng cửu chương
read -p "nhập một số nguyên: " number
echo "bảng cửu chương của $number:"

# in bảng cửu chương
for i in {1..10}; do
    echo "$number x $i = $(($number * $i))"
done
COMMENT

<<COMMENT
# in ra tất cả bảng cửu chương
for i in {2..9}; do
    echo "bảng cửu chương của $i:"
    for j in {1..10}; do
        echo "$i x $j = $(($i * $j))"
    done
    echo "------------------------"
done
COMMENT

# chuyển số thập phân sang số nhị phân
# nhập số thập phân
read -p "nhập một số nguyên dương: " number
num=$number

i chuyển số thập phân sang số nhị phân
binary=""
while [ $number -gt 0 ]; do
    remainder=$(($number % 2))
    binary="$remainder$binary"
    number=$((number/ 2))
done
echo "$num ở hệ nhị phân: $binary"